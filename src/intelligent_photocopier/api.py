"""
Flask API for AI Course Builder web interface.

Provides REST endpoints for creating courses through the web UI.
"""

import logging
import os
import subprocess

from flask import Flask, jsonify, request
from flask_cors import CORS
from github import Github

from .course_generator import CourseGenerator

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


@app.route("/api/generate-course", methods=["POST"])
def generate_course():
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
        course_info = {
            "course_id": course_id,
            "id": course_id,  # Keep both for compatibility
            "title": title,
            "level": level,
            "duration": duration,
            "description": description or f"A comprehensive {level.lower()} course on {title}",
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
            if key == "README.md" or key == "readme":
                rel_path = "README.md"
            elif key == "lesson-content.md" or key == "lesson_content":
                rel_path = "lesson-content.md"
            elif key == "summary.md" or key == "summary":
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


def _commit_to_github(course_id: str, files_content: dict[str, str]):
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

            # Add to tree elements with proper mode for files
            tree_elements.append(
                {
                    "path": github_path,
                    "mode": "100644",  # Regular file mode
                    "type": "blob",
                    "sha": blob.sha,
                }
            )
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
        result = subprocess.run(
            ["npm", "run", "build"], capture_output=True, text=True, timeout=60, check=False
        )
        if result.returncode == 0:
            logger.info("Site rebuilt successfully")
        else:
            logger.warning(f"Site rebuild failed: {result.stderr}")
    except Exception as e:
        logger.error(f"Error rebuilding site: {e}")


def run_server(host: str = "0.0.0.0", port: int = 5000, debug: bool = False):
    """Run the Flask API server."""
    logger.info(f"Starting AI Course Builder API on {host}:{port}")
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    run_server(debug=True)
