"""
Simple test script to verify the Intelligent Photocopier components work.
"""

import sys
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from intelligent_photocopier.content_analyzer import ContentAnalyzer
from intelligent_photocopier.template_extractor import TemplateExtractor


def test_content_analyzer():
    """Test the ContentAnalyzer with sample input."""
    print("🧪 Testing Content Analyzer...")

    sample_content = """
# B2: Performance Optimization

Learn to write high-performance Python code that scales efficiently and runs fast.

## Learning Objectives
- Profile and identify performance bottlenecks
- Optimize algorithms and data structures
- Implement memory management techniques
- Use caching strategies effectively
- Apply parallel processing concepts

Duration: 4-5 hours
Level: Intermediate
    """

    analyzer = ContentAnalyzer()
    course_info = analyzer.extract_course_info(sample_content)

    print(f"✅ Course ID: {course_info['course_id']}")
    print(f"✅ Title: {course_info['title']}")
    print(f"✅ Objectives: {len(course_info['objectives'])} found")
    print(f"✅ Duration: {course_info['duration']}")
    print(f"✅ Level: {course_info['level']}")
    print()


def test_template_extractor():
    """Test the TemplateExtractor with A1 course."""
    print("🧪 Testing Template Extractor...")

    template_path = Path("../../Lessons/A1-Defensive-Programming")

    if not template_path.exists():
        print("❌ A1 course not found. Skipping template extractor test.")
        return

    extractor = TemplateExtractor(template_path)

    try:
        structure = extractor.extract_structure()
        print(f"✅ Found {len(structure['files']['files'])} files")
        print(f"✅ Found {len(structure['files']['directories'])} directories")
        print(f"✅ Extracted {len(structure['content_patterns'])} content patterns")
        print()
    except Exception as e:
        print(f"❌ Template extraction failed: {e}")


def main():
    """Run basic component tests."""
    print("🤖 Intelligent Photocopier - Component Tests")
    print("=" * 50)
    print()

    test_content_analyzer()
    test_template_extractor()

    print("🎉 Basic component tests completed!")
    print("\nNext: Implement CourseGenerator and FileManager components.")


if __name__ == "__main__":
    main()
