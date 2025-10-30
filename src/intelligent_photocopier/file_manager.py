"""
File Manager - Handles creation and organization of course files.

This module manages the file system operations for creating
new course directories and files.
"""

import os
from pathlib import Path
from typing import Dict, Any


class FileManager:
    """Manages file creation and organization for generated courses."""

    def __init__(self, lessons_base_path: Path):
        """Initialize with base path for lessons."""
        self.lessons_path = Path(lessons_base_path)

    def create_course(self, course_id: str, generated_content: Dict[str, str]) -> Path:
        """Create a complete course directory structure with content."""
        course_path = self.lessons_path / course_id

        # Create main course directory
        course_path.mkdir(exist_ok=True)

        # Create subdirectories
        self._create_directory_structure(course_path)

        # Create main content files (includes AI-generated reference and solutions)
        self._create_content_files(course_path, generated_content)

        # Create placeholder files for practice modules
        self._create_practice_files(course_path, course_id)

        return course_path

    def _create_directory_structure(self, course_path: Path):
        """Create the standard directory structure."""
        directories = [
            "tests",
            "solutions",
            "reference"
        ]

        for directory in directories:
            (course_path / directory).mkdir(exist_ok=True)

    def _create_content_files(self, course_path: Path, content: Dict[str, str]):
        """Create main content files with generated content."""
        for filename, file_content in content.items():
            file_path = course_path / filename
            
            # Create parent directories if they don't exist
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_content)

    def _create_practice_files(self, course_path: Path, course_id: str):
        """Create placeholder practice module files."""
        tests_dir = course_path / "tests"

        # Create a basic practice module (placeholder)
        practice_module = f"""\"\"\"
Practice module for {course_id} course.

This module contains exercises and practice code for the lesson.
Students will enhance this code by applying the concepts learned.
\"\"\"

# TODO: AI will generate topic-specific practice exercises


def example_function():
    \"\"\"Example function for practice.\"\"\"
    # TODO: Implement according to lesson requirements
    pass


class ExampleClass:
    \"\"\"Example class for practice exercises.\"\"\"

    def __init__(self):
        \"\"\"Initialize the example class.\"\"\"
        # TODO: Add initialization code
        pass

    def example_method(self):
        \"\"\"Example method for practice.\"\"\"
        # TODO: Implement according to lesson requirements
        pass


if __name__ == "__main__":
    # Example usage
    print(f"Practice module for {course_id} course")
    example = ExampleClass()
    example.example_method()
"""

        with open(tests_dir / "practice_module.py", 'w') as f:
            f.write(practice_module)

        # Create basic test file
        test_file = f"""\"\"\"
Tests for {course_id} practice exercises.

This file contains tests to validate the practice exercises
and guide students through the learning process.
\"\"\"

import pytest
from .practice_module import example_function, ExampleClass


class TestPracticeModule:
    \"\"\"Test the practice module implementation.\"\"\"

    def test_example_function(self):
        \"\"\"Test the example function.\"\"\"
        # TODO: Add meaningful tests based on course objectives
        assert example_function() is not None

    def test_example_class(self):
        \"\"\"Test the example class.\"\"\"
        example = ExampleClass()
        assert example is not None

        # TODO: Add tests for class methods
        result = example.example_method()
        assert result is not None


# TODO: AI will generate course-specific test cases
"""

        with open(tests_dir / "test_practice.py", 'w') as f:
            f.write(test_file)

    def _create_reference_files(self, course_path: Path):
        """Create reference and guide files."""
        reference_dir = course_path / "reference"

        # Exercise instructions
        exercise_instructions = """# Exercise Instructions

## Overview
This exercise will guide you through applying the concepts learned in this lesson.

## Your Tasks

### Phase 1: Analysis (15 minutes)
1. **Study the provided modules**
2. **Identify areas for improvement**
3. **Plan your implementation strategy**

### Phase 2: Implementation (60 minutes)
4. **Apply the learned concepts**
5. **Enhance the practice modules**
6. **Test your implementation**

### Phase 3: Validation (15 minutes)
7. **Run comprehensive tests**
8. **Review and refine**
9. **Document your learnings**

## Success Criteria
Your implementation is complete when:
- [ ] All tests pass
- [ ] Code follows best practices
- [ ] Implementation demonstrates course concepts

## Tips for Success
1. Start small and iterate
2. Test frequently
3. Apply the patterns learned in the lesson
4. Refer to the lesson content as needed

## Next Steps
After completing this exercise, review the solutions and consider how to apply these concepts to your own projects.
"""

        with open(reference_dir / "exercise_instructions.md", 'w') as f:
            f.write(exercise_instructions)

        # Quick reference
        quick_reference = """# Quick Reference

## Key Concepts
// TODO: AI will generate topic-specific quick reference

## Common Patterns
// TODO: AI will generate common implementation patterns

## Best Practices
// TODO: AI will generate best practices for the topic

## Troubleshooting
// TODO: AI will generate common issues and solutions
"""

        with open(reference_dir / "quick_reference.md", 'w') as f:
            f.write(quick_reference)

        # Best practices
        best_practices = """# Best Practices

## Core Principles
// TODO: AI will generate topic-specific best practices

## Implementation Guidelines
// TODO: AI will generate implementation guidelines

## Performance Considerations
// TODO: AI will generate performance tips

## Security Considerations
// TODO: AI will generate security considerations if applicable
"""

        with open(reference_dir / "best_practices.md", 'w') as f:
            f.write(best_practices)

    def update_main_readme(self, course_id: str, course_title: str):
        """Update the main project README to include the new course."""
        # TODO: Implement README update logic
        pass
