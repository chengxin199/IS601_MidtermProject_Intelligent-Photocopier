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
CORS(app)  # Enable CORS for web interface


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
            "id": course_id,
            "title": title,
            "level": level,
            "duration": duration,
            "description": description,
            "source_material": content,
            "learning_objectives": _extract_objectives(content),
            "topics": _extract_topics(content),
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

        # README.md
        if "readme" in generated_content:
            readme_path = output_dir / "README.md"
            readme_path.write_text(generated_content["readme"], encoding="utf-8")
            files_created.append("README.md")

        # lesson-content.md
        if "lesson_content" in generated_content:
            lesson_path = output_dir / "lesson-content.md"
            lesson_path.write_text(generated_content["lesson_content"], encoding="utf-8")
            files_created.append("lesson-content.md")

        # summary.md
        if sections.get("summary") and "summary" in generated_content:
            summary_path = output_dir / "summary.md"
            summary_path.write_text(generated_content["summary"], encoding="utf-8")
            files_created.append("summary.md")

        # reference/
        if sections.get("reference") and "reference" in generated_content:
            ref_dir = output_dir / "reference"
            ref_dir.mkdir(exist_ok=True)
            ref_path = ref_dir / "quick-reference.md"
            ref_path.write_text(generated_content["reference"], encoding="utf-8")
            files_created.append("reference/quick-reference.md")

        # solutions/
        if sections.get("solutions") and "solutions" in generated_content:
            sol_dir = output_dir / "solutions"
            sol_dir.mkdir(exist_ok=True)
            sol_path = sol_dir / "exercise-solutions.md"
            sol_path.write_text(generated_content["solutions"], encoding="utf-8")
            files_created.append("solutions/exercise-solutions.md")

        # tests/
        if sections.get("tests") and "tests" in generated_content:
            test_dir = output_dir / "tests"
            test_dir.mkdir(exist_ok=True)
            test_path = test_dir / "practice-tests.md"
            test_path.write_text(generated_content["tests"], encoding="utf-8")
            files_created.append("tests/practice-tests.md")

        logger.info(f"Course created successfully: {output_dir}")

        # Optionally rebuild Eleventy site
        try:
            _rebuild_site()
        except Exception as e:
            logger.warning(f"Failed to rebuild site: {e}")

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
