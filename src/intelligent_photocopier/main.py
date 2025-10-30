"""
Main entry point for the Intelligent Photocopier course generator.

This module provides the primary interface for generating new courses
based on user input and existing templates.
"""

import sys
from pathlib import Path

from .config import config
from .content_analyzer import ContentAnalyzer
from .course_generator import CourseGenerator
from .file_manager import FileManager
from .template_extractor import TemplateExtractor


class IntelligentPhotocopier:
    """Main class for the Intelligent Photocopier course generation system."""

    def __init__(self, base_path: str | None = None):
        """Initialize the photocopier with the base project path."""
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.lessons_path = self.base_path / "Lessons"
        self.template_source = self.lessons_path / "A1-Defensive-Programming-Template"

        # Initialize components
        self.analyzer = ContentAnalyzer()
        self.template_extractor = TemplateExtractor(self.template_source)
        self.course_generator = CourseGenerator()
        self.file_manager = FileManager(self.lessons_path)

    def run_interactive(self):
        """Run the interactive course generation process."""
        print("🤖 Intelligent Photocopier - AI Course Generator")
        print("=" * 50)

        # Check configuration
        if not config.is_configured():
            print("⚠️  Configuration Required")
            print()
            missing = config.get_missing_config()
            for item in missing:
                print(f"❌ {item}")
            print()
            print("📋 To set up:")
            print("1. Copy .env.example to .env")
            print("2. Add your OpenAI API key to the .env file")
            print("3. Get API key from: https://platform.openai.com/api-keys")
            print()

            # Create sample .env file
            sample_path = config.create_sample_env_file()
            print(f"📄 Sample configuration created: {sample_path}")
            print()

            use_placeholder = input("Continue with placeholder content? (y/N): ").lower().strip()
            if use_placeholder != "y":
                print("Exiting. Please configure API key and try again.")
                return False
            else:
                print("⚠️  Using placeholder content (limited functionality)")
                print()
        else:
            print("✅ OpenAI API configured")
            print()

        print("Please paste your complete course README content below.")
        print("(Press Ctrl+D when finished, or type 'END' on a new line)")
        print("-" * 50)

        # Collect user input
        content_lines = []
        try:
            while True:
                try:
                    line = input()
                    if line.strip() == "END":
                        break
                    content_lines.append(line)
                except EOFError:
                    break
        except KeyboardInterrupt:
            print("\n❌ Generation cancelled by user.")
            return False

        if not content_lines:
            print("❌ No content provided. Exiting.")
            return False

        user_content = "\n".join(content_lines)

        print("\n🔍 Analyzing course content...")
        return self.generate_course(user_content)

    def generate_course(self, user_content: str) -> bool:
        """Generate a course based on user content."""
        try:
            # Step 1: Analyze user input
            course_info = self.analyzer.extract_course_info(user_content)
            print(f"📊 Detected Course: {course_info['title']}")
            print(f"🎯 Learning Objectives: {len(course_info['objectives'])} identified")

            # Step 2: Extract template structure
            print("📋 Extracting template structure...")
            template_structure = self.template_extractor.extract_structure()

            # Step 3: Generate course content
            print("🤖 Generating course content with AI...")
            generated_content = self.course_generator.generate_course_content(
                course_info, template_structure
            )

            # Step 4: Create files
            print("📁 Creating course files...")
            course_path = self.file_manager.create_course(
                course_info["course_id"], generated_content
            )

            print(f"✅ Course '{course_info['title']}' generated successfully!")
            print(f"📍 Location: {course_path}")
            print(f"🚀 Ready to learn at: Lessons/{course_info['course_id']}/")

            return True

        except Exception as e:
            print(f"❌ Error generating course: {e}")
            return False


def main():
    """CLI entry point for the Intelligent Photocopier."""
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
        print(
            """
🤖 Intelligent Photocopier - AI Course Generator

Usage:
    python -m src.intelligent_photocopier.main

Interactive mode:
    The program will prompt you to paste your course content.
    Provide a complete course description and learning objectives.

Example input:
    # B2: Performance Optimization
    Learn to write high-performance Python code...

    ## Learning Objectives
    - Profile and identify bottlenecks
    - Optimize algorithms and data structures
    - Memory management techniques
    ...
        """
        )
        return

    photocopier = IntelligentPhotocopier()
    photocopier.run_interactive()


if __name__ == "__main__":
    main()
