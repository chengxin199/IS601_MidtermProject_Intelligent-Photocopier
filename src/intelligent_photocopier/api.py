"""
Flask API for AI Course Builder web interface.

Provides REST endpoints for creating courses through the web UI.
"""

import logging
import os
import subprocess  # nosec B404 - Used safely with fixed command list

from flask import Flask, jsonify, request
from flask_cors import CORS
from github import Github, InputGitTreeElement

from .auth import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    optional_auth,
    require_auth,
    verify_password,
)
from .course_generator import CourseGenerator
from .models import Course, User, init_db

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
# Enable CORS for production domain and localhost
CORS(
    app,
    origins=[
        "http://localhost:8080",
        "http://localhost:8081",
        "https://intelligentphotocopier.online",
        "http://intelligentphotocopier.online",
        "https://www.intelligentphotocopier.online",
        "http://www.intelligentphotocopier.online",
        "https://intelligentphotocopier.netlify.app",
    ],
)

# Initialize database
engine, SessionLocal = init_db()


def get_db():
    """Get database session."""
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


@app.route("/", methods=["GET", "HEAD"])
def root():
    """Root endpoint for health checks."""
    return jsonify({
        "service": "Intelligent Photocopier API",
        "status": "running",
        "version": "1.0.8",
        "endpoints": {
            "health": "/api/health",
            "docs": "https://intelligentphotocopier.online"
        }
    })


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "ok", "service": "AI Course Builder API"})


@app.route("/api/debug", methods=["GET"])
def debug_info():
    """Debug endpoint to check environment."""
    github_token = os.getenv("GITHUB_TOKEN")
    openai_key = os.getenv("OPENAI_API_KEY")
    return jsonify(
        {
            "github_token_set": bool(github_token),
            "github_token_length": len(github_token) if github_token else 0,
            "openai_key_set": bool(openai_key),
            "openai_key_length": len(openai_key) if openai_key else 0,
        }
    )


# ============================================================================
# Authentication Endpoints
# ============================================================================


@app.route("/api/auth/register", methods=["POST"])
def register():
    """Register a new user."""
    data = request.get_json()

    # Validate input and check for errors
    error_response = _validate_registration_data(data)
    if error_response:
        return error_response

    username = data["username"].strip()
    email = data["email"].strip().lower()
    password = data["password"]

    db = get_db()

    # Check if user already exists
    existing_user = (
        db.query(User).filter((User.username == username) | (User.email == email)).first()
    )

    if existing_user:
        error_msg = (
            "Username already taken"
            if existing_user.username == username
            else "Email already registered"
        )
        return jsonify({"error": error_msg}), 409

    # Create new user
    hashed_pw = hash_password(password)
    new_user = User(
        username=username,
        email=email,
        password_hash=hashed_pw,
        full_name=data.get("full_name", ""),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Generate tokens
    access_token = create_access_token(int(new_user.id), str(new_user.username))  # type: ignore
    refresh_token = create_refresh_token(int(new_user.id), str(new_user.username))  # type: ignore

    return (
        jsonify(
            {
                "message": "User registered successfully",
                "user": new_user.to_dict(include_email=True),
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
        ),
        201,
    )


def _validate_registration_data(data):
    """Validate registration data. Returns error response or None."""
    required_fields = ["username", "email", "password"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    username = data["username"].strip()
    email = data["email"].strip().lower()
    password = data["password"]

    if len(username) < 3:
        return jsonify({"error": "Username must be at least 3 characters"}), 400
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400
    if "@" not in email:
        return jsonify({"error": "Invalid email address"}), 400

    return None


@app.route("/api/auth/login", methods=["POST"])
def login():
    """Login user and return JWT tokens."""
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data["username"].strip()
    password = data["password"]

    db = get_db()

    # Find user by username or email
    user = db.query(User).filter((User.username == username) | (User.email == username)).first()

    if not user or not verify_password(password, user.password_hash):
        return jsonify({"error": "Invalid credentials"}), 401

    if not user.is_active:
        return jsonify({"error": "Account is disabled"}), 403

    # Generate tokens
    access_token = create_access_token(user.id, user.username)
    refresh_token = create_refresh_token(user.id, user.username)

    return jsonify(
        {
            "message": "Login successful",
            "user": user.to_dict(include_email=True),
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
    )


@app.route("/api/auth/refresh", methods=["POST"])
def refresh():
    """Refresh access token using refresh token."""
    data = request.get_json()

    if not data or "refresh_token" not in data:
        return jsonify({"error": "Missing refresh token"}), 400

    refresh_token = data["refresh_token"]
    payload = decode_token(refresh_token)

    if not payload or payload.get("type") != "refresh":
        return jsonify({"error": "Invalid refresh token"}), 401

    # Generate new access token
    access_token = create_access_token(payload["user_id"], payload["username"])

    return jsonify({"access_token": access_token})


@app.route("/api/auth/me", methods=["GET"])
@require_auth
def get_current_user():
    """Get current user profile."""
    db = get_db()
    user = db.query(User).filter(User.id == request.user_id).first()  # type: ignore

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"user": user.to_dict(include_email=True)})


# ============================================================================
# User Profile Endpoints
# ============================================================================


@app.route("/api/profile", methods=["PUT"])
@require_auth
def update_profile():
    """Update user profile."""
    data = request.get_json()
    db = get_db()

    user = db.query(User).filter(User.id == request.user_id).first()  # type: ignore
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Update allowed fields
    if "full_name" in data:
        user.full_name = data["full_name"].strip()
    if "bio" in data:
        user.bio = data["bio"].strip()
    if "avatar_url" in data:
        user.avatar_url = data["avatar_url"].strip()

    db.commit()
    db.refresh(user)

    return jsonify(
        {"message": "Profile updated successfully", "user": user.to_dict(include_email=True)}
    )


# ============================================================================
# Course Management Endpoints
# ============================================================================


@app.route("/api/courses/my", methods=["GET"])
@require_auth
def get_my_courses():
    """Get all courses created by the current user."""
    db = get_db()

    courses = (
        db.query(Course)
        .filter(Course.user_id == request.user_id)  # type: ignore
        .order_by(Course.created_at.desc())
        .all()
    )

    return jsonify({"courses": [course.to_dict() for course in courses]})


# ============================================================================
# Admin/Debug Endpoints
# ============================================================================


@app.route("/api/admin/users", methods=["GET"])
def list_users():
    """List all registered users (for debugging)."""
    db = get_db()
    users = db.query(User).order_by(User.created_at.desc()).all()

    return jsonify(
        {
            "total": len(users),
            "users": [
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "full_name": user.full_name,
                    "created_at": user.created_at.isoformat() if user.created_at else None,
                    "courses_count": len(user.courses),
                }
                for user in users
            ],
        }
    )


@app.route("/api/admin/stats", methods=["GET"])
def get_stats():
    """Get system statistics."""
    db = get_db()

    total_users = db.query(User).count()
    total_courses = db.query(Course).count()
    courses_with_users = db.query(Course).filter(Course.user_id.isnot(None)).count()
    anonymous_courses = db.query(Course).filter(Course.user_id.is_(None)).count()

    # Recent registrations (last 7 days)
    from datetime import datetime, timedelta, timezone

    seven_days_ago = datetime.now(timezone.utc) - timedelta(days=7)
    recent_users = db.query(User).filter(User.created_at >= seven_days_ago).count()

    return jsonify(
        {
            "users": {
                "total": total_users,
                "recent_7_days": recent_users,
            },
            "courses": {
                "total": total_courses,
                "with_users": courses_with_users,
                "anonymous": anonymous_courses,
            },
        }
    )


@app.route("/api/generate-course", methods=["POST"])
@optional_auth
def generate_course():  # pylint: disable=too-many-locals
    """
    Generate a course from provided material.

    Expected JSON payload:
    {
        "courseId": "B3-design-patterns",
        "title": "Advanced Design Patterns",
        "level": "Intermediate",
        "duration": "3-4 hours",
        "description": "Learn advanced design patterns...",
        "content": "Course outline and material...",
        "sections": {
            "summary": true,
            "reference": true,
            "solutions": true,
            "tests": true
        }
    }
    """
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ["courseId", "title", "content"]
        missing_fields = [f for f in required_fields if f not in data]
        if missing_fields:
            return (
                jsonify(
                    {
                        "success": False,
                        "error": f"Missing required fields: {', '.join(missing_fields)}",
                    }
                ),
                400,
            )

        # Extract data
        course_id = data["courseId"]
        title = data["title"]
        level = data.get("level", "Intermediate")
        duration = data.get("duration", "3-4 hours")
        description = data.get("description", "")
        content = data["content"]
        sections = data.get("sections", {})

        # Initialize generator
        generator = CourseGenerator()

        # Prepare course info
        # Generate a more natural description if not provided
        if not description:
            # Extract first meaningful sentence from content as description
            first_lines = content.split("\n")[:5]
            desc_candidate = " ".join(first_lines).strip()
            # Clean up and limit length
            desc_candidate = desc_candidate.replace("#", "").strip()
            description = (
                desc_candidate[:150] + "..."
                if len(desc_candidate) > 150
                else desc_candidate
                or f"Learn {title} with practical examples and hands-on exercises"
            )

        course_info = {
            "course_id": course_id,
            "id": course_id,  # Keep both for compatibility
            "title": title,
            "level": level,
            "duration": duration,
            "description": description,
            "source_material": content,
            "objectives": _extract_objectives(content),
            "learning_objectives": _extract_objectives(content),  # Keep both
            "topics": _extract_topics(content),
            "prerequisites": ["Basic programming knowledge", "Familiarity with Python"],
        }

        # Define template structure based on selected sections
        template_structure = {
            "readme": {"required": True},
            "lesson_content": {"required": True},
            "summary": {"required": sections.get("summary", True)},
            "reference": {"required": sections.get("reference", True)},
            "solutions": {"required": sections.get("solutions", True)},
            "tests": {"required": sections.get("tests", True)},
        }

        logger.info(f"Generating course: {course_id}")

        # Generate course content
        generated_content = generator.generate_course_content(course_info, template_structure)

        # Prepare files for GitHub commit
        files_to_commit = {}

        # Process generated content - handle both dict keys and file paths
        for key, content in generated_content.items():
            if not content:
                continue

            # Determine file path
            if key in ("README.md", "readme"):
                rel_path = "README.md"
            elif key in ("lesson-content.md", "lesson_content"):
                rel_path = "lesson-content.md"
            elif key in ("summary.md", "summary"):
                rel_path = "summary.md"
            elif "/" in key:  # Handle paths like "reference/quick_reference.md"
                rel_path = key
            else:
                # Skip unknown keys
                continue

            files_to_commit[rel_path] = content

        logger.info(f"Course content generated: {len(files_to_commit)} files")

        # Commit to GitHub to trigger Netlify rebuild
        github_success = _commit_to_github(course_id, files_to_commit)

        # Save course to database if user is authenticated
        if hasattr(request, "user_id") and request.user_id:  # type: ignore
            db = get_db()
            new_course = Course(
                course_id=course_id,
                title=title,
                description=description,
                level=level,
                duration=duration,
                github_url=(
                    f"https://github.com/chengxin199/"
                    f"Intelligent-Photocopier/tree/main/Lessons/{course_id}"
                ),
                deployed_url=(f"https://intelligentphotocopier.online/" f"Lessons/{course_id}/"),
                user_id=request.user_id,  # type: ignore
            )
            db.add(new_course)
            db.commit()
            logger.info(
                f"Course {course_id} saved to database "
                f"for user {request.user_id}"  # type: ignore
            )

        return jsonify(
            {
                "success": True,
                "courseId": course_id,
                "filesCreated": list(files_to_commit.keys()),
                "githubCommitted": github_success,
                "message": f"Course '{title}' generated successfully!",
                "content": files_to_commit,  # Return content for immediate preview
            }
        )

    except Exception as e:
        logger.error(f"Error generating course: {e}", exc_info=True)
        return jsonify({"success": False, "error": str(e)}), 500


def _extract_objectives(content: str) -> list[str]:
    """Extract learning objectives from content."""
    objectives = []
    lines = content.split("\n")
    in_objectives = False

    for line in lines:
        line = line.strip()
        if "learning objective" in line.lower() or "objectives" in line.lower():
            in_objectives = True
            continue
        if in_objectives:
            if line.startswith("-") or line.startswith("*"):
                objectives.append(line.lstrip("-*").strip())
            elif line.startswith("#") or (objectives and not line):
                break

    if not objectives:
        objectives = [
            "Master key concepts",
            "Apply practical techniques",
            "Build real-world projects",
        ]

    return objectives[:6]  # Limit to 6 objectives


def _extract_topics(content: str) -> list[str]:
    """Extract main topics from content."""
    topics = []
    lines = content.split("\n")

    for line in lines:
        line = line.strip()
        # Look for markdown headers or numbered items
        if line.startswith("## ") and "topic" in line.lower():
            topics.append(line.lstrip("#").strip())
        elif line.startswith(("1.", "2.", "3.", "4.", "5.")):
            topics.append(line.split(".", 1)[1].strip())

    if not topics:
        topics = [
            "Introduction",
            "Core Concepts",
            "Advanced Techniques",
            "Best Practices",
            "Summary",
        ]

    return topics[:8]  # Limit to 8 topics


def _commit_to_github(  # pylint: disable=too-many-locals
    course_id: str, files_content: dict[str, str]
):
    """Commit generated course files to GitHub repository as a single batch commit.

    Args:
        course_id: The course ID
        files_content: Dict mapping relative file paths to their content
    """
    try:
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            logger.warning("GITHUB_TOKEN not set, skipping GitHub commit")
            return False

        # Initialize GitHub client
        g = Github(github_token)
        repo = g.get_repo("chengxin199/Intelligent-Photocopier")

        logger.info(f"Committing course {course_id} to GitHub as single batch commit...")

        # Get the default branch and its latest commit
        branch = repo.default_branch
        branch_ref = repo.get_branch(branch)
        base_commit = branch_ref.commit
        base_tree = base_commit.commit.tree

        # Create blobs and tree elements for all files
        tree_elements = []
        for file_rel_path, content in files_content.items():
            github_path = f"Lessons/{course_id}/{file_rel_path}"

            # Create a blob for the file content
            blob = repo.create_git_blob(content, "utf-8")

            # Add to tree elements using InputGitTreeElement
            tree_element = InputGitTreeElement(
                path=github_path, mode="100644", type="blob", sha=blob.sha
            )
            tree_elements.append(tree_element)
            logger.info(f"✓ Prepared blob for {github_path}")

        # Create a new tree with all the files
        new_tree = repo.create_git_tree(tree_elements, base_tree)
        logger.info(f"Created git tree with {len(tree_elements)} files")

        # Create a single commit with all changes
        commit_message = f"Add generated course: {course_id}"
        new_commit = repo.create_git_commit(commit_message, new_tree, [base_commit.commit])
        logger.info(f"Created commit: {new_commit.sha}")

        # Update the branch reference to point to the new commit
        ref = repo.get_git_ref(f"heads/{branch}")
        ref.edit(new_commit.sha)

        logger.info(f"Successfully committed course {course_id} to GitHub in single commit")
        return True

    except Exception as e:
        logger.error(f"Failed to commit to GitHub: {e}")
        return False


def _rebuild_site():
    """Rebuild the Eleventy static site."""
    try:
        logger.info("Rebuilding Eleventy site...")
        # Fixed command list with no user input - safe to use
        result = subprocess.run(  # nosec B603 B607
            ["npm", "run", "build"], capture_output=True, text=True, timeout=60, check=False
        )
        if result.returncode == 0:
            logger.info("Site rebuilt successfully")
        else:
            logger.warning(f"Site rebuild failed: {result.stderr}")
    except Exception as e:
        logger.error(f"Error rebuilding site: {e}")


def run_server(host: str = "0.0.0.0", port: int = 5000, debug: bool = False):  # nosec B104
    """Run the Flask API server.

    Args:
        host: Bind to 0.0.0.0 for Docker/container deployment (intentional)
        port: Port to listen on
        debug: Enable debug mode
    """
    logger.info(f"Starting AI Course Builder API on {host}:{port}")
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    # Get port from environment variable (for Render.com, Heroku, etc.)
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_ENV", "development") != "production"
    run_server(port=port, debug=debug)
