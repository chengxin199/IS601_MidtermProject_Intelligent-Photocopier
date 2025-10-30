"""
Test script for OpenAI API integration.

This script tests the OpenAI API connection and basic functionality
before running the full course generation.
"""

import sys
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from intelligent_photocopier.config import config
from intelligent_photocopier.course_generator import CourseGenerator


def test_api_connection():
    """Test the OpenAI API connection."""
    print("🔧 Testing OpenAI API Connection")
    print("=" * 40)
    print()

    # Check configuration
    print("📋 Configuration Status:")
    if config.is_configured():
        print("✅ OpenAI API Key: Configured")
        print(f"✅ Model: {config.model}")
        print(f"✅ Max Tokens: {config.max_tokens}")
        print(f"✅ Temperature: {config.temperature}")
    else:
        print("❌ Configuration Issues:")
        for item in config.get_missing_config():
            print(f"   - {item}")
        print("\n💡 To fix: Copy .env.example to .env and add your API key")
        return False

    print()

    # Test basic API call
    print("🔍 Testing API Connection...")
    try:
        generator = CourseGenerator()

        if not generator.client:
            print("❌ OpenAI client not initialized")
            return False

        # Test with a simple prompt
        test_response = generator.client.chat.completions.create(
            model=config.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello and confirm you're working!"}
            ],
            max_tokens=50,
            temperature=0.7
        )

        content = test_response.choices[0].message.content
        response_text = content.strip() if content else "No response"

        print("✅ API Connection Successful!")
        print(f"🤖 Response: {response_text}")
        print()

        return True

    except Exception as e:
        print(f"❌ API Connection Failed: {e}")
        print("\n💡 Check your API key and internet connection")
        return False


def test_course_generation():
    """Test the course generation with a simple example."""
    print("🎓 Testing Course Generation")
    print("=" * 40)
    print()

    # Simple test course info
    test_course_info = {
        "course_id": "TEST",
        "title": "API Testing Basics",
        "description": "Learn how to test APIs effectively",
        "objectives": [
            "Understand API testing principles",
            "Write effective test cases"
        ],
        "duration": "2 hours",
        "level": "Beginner",
        "topics": ["API Testing", "Test Cases"],
        "prerequisites": ["Basic programming knowledge"]
    }

    try:
        generator = CourseGenerator()

        print("🤖 Generating test README content...")
        readme_content = generator._generate_ai_readme(test_course_info, {})

        print("✅ Test Generation Successful!")
        print("📄 Sample Content Preview:")
        print("-" * 30)
        print(readme_content[:300] + "..." if len(readme_content) > 300 else readme_content)
        print("-" * 30)
        print()

        return True

    except Exception as e:
        print(f"❌ Course Generation Failed: {e}")
        return False


def main():
    """Run API tests."""
    print("🧪 Intelligent Photocopier - API Integration Tests")
    print("=" * 60)
    print()

    # Test 1: API Connection
    api_ok = test_api_connection()

    if not api_ok:
        print("🚫 Skipping course generation test due to API issues")
        return

    # Test 2: Course Generation
    generation_ok = test_course_generation()

    # Summary
    print("📊 Test Summary:")
    print(f"   API Connection: {'✅ PASS' if api_ok else '❌ FAIL'}")
    print(f"   Course Generation: {'✅ PASS' if generation_ok else '❌ FAIL'}")
    print()

    if api_ok and generation_ok:
        print("🎉 All tests passed! Ready for full course generation.")
    else:
        print("⚠️  Some tests failed. Please check configuration and try again.")


if __name__ == "__main__":
    main()
