"""
Flask API for AI Course Builder web interface.

Provides REST endpoints for creating courses through the web UI.
"""

import logging
import subprocess
from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS

from .course_generator import CourseGenerator

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
# Enable CORS for production domain and localhost
CORS(app, origins=[
    "http://localhost:8080",
    "http://localhost:8081",
    "https://intelligentphotocopier.online",
    "http://intelligentphotocopier.online",
    "https://www.intelligentphotocopier.online",
    "http://www.intelligentphotocopier.online",
    "https://intelligentphotocopier.netlify.app"
])


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "ok", "service": "AI Course Builder API"})


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
            return jsonify({
                "success": False,
                "error": f"Missing required fields: {', '.join(missing_fields)}"
            }), 400

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
        generated_content = generator.generate_course_content(
            course_info, template_structure
        )

        # Create output directory
        output_dir = Path("Lessons") / course_id
        output_dir.mkdir(parents=True, exist_ok=True)        # Write files
        files_created = []

        # Process generated content - handle both dict keys and file paths
        for key, content in generated_content.items():
            if not content:
                continue

            # Determine file path
            if key == "README.md" or key == "readme":
                file_path = output_dir / "README.md"
            elif key == "lesson-content.md" or key == "lesson_content":
                file_path = output_dir / "lesson-content.md"
            elif key == "summary.md" or key == "summary":
                file_path = output_dir / "summary.md"
            elif "/" in key:  # Handle paths like "reference/quick_reference.md"
                file_path = output_dir / key
            else:
                # Skip unknown keys
                continue

            # Create parent directories if needed
            file_path.parent.mkdir(parents=True, exist_ok=True)

            # Write content
            file_path.write_text(content, encoding="utf-8")
            files_created.append(str(file_path.relative_to(output_dir)))

        logger.info(f"Course created successfully: {output_dir}")

        # Skip rebuilding site when using eleventy --serve
        # BrowserSync will auto-refresh when it detects file changes
        # Uncommment the lines below if you need manual rebuild
        # try:
        #     _rebuild_site()
        # except Exception as e:
        #     logger.warning(f"Failed to rebuild site: {e}")

        return jsonify({
            "success": True,
            "courseId": course_id,
            "path": str(output_dir),
            "filesCreated": files_created,
            "message": f"Course '{title}' generated successfully!"
        })

    except Exception as e:
        logger.error(f"Error generating course: {e}", exc_info=True)
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


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
        objectives = ["Master key concepts", "Apply practical techniques", "Build real-world projects"]

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
        topics = ["Introduction", "Core Concepts", "Advanced Techniques", "Best Practices", "Summary"]

    return topics[:8]  # Limit to 8 topics


def _rebuild_site():
    """Rebuild the Eleventy static site."""
    try:
        logger.info("Rebuilding Eleventy site...")
        result = subprocess.run(
            ["npm", "run", "build"],
            capture_output=True,
            text=True,
            timeout=60,
            check=False
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
