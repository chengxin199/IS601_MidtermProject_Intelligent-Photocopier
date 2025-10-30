#!/usr/bin/env python3
"""
Quick Start script for Intelligent Photocopier.

This script provides a simple way to get started with the AI course generator.
"""

import sys
from pathlib import Path

from src.intelligent_photocopier.config import config
from src.intelligent_photocopier.test_api import test_api_connection

# Add src to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))


def print_banner():
    """Print the welcome banner."""
    print("🤖 Intelligent Photocopier - Quick Start")
    print("=" * 50)
    print("AI-powered course generator based on A1 template")
    print()


def check_setup():
    """Check if the system is set up correctly."""
    print("🔧 System Check")
    print("-" * 20)

    # Check if .env exists
    env_file = project_root / ".env"
    if not env_file.exists():
        print("❌ .env file not found")
        print()
        print("📋 Setup Required:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key to .env")
        print("3. Get API key: https://platform.openai.com/api-keys")
        print()

        # Offer to create .env file
        create_env = input("Create .env file from template? (Y/n): ").lower().strip()
        if create_env in ["", "y", "yes"]:
            import shutil

            shutil.copy(project_root / ".env.example", env_file)
            print(f"✅ Created {env_file}")
            print("📝 Please edit .env and add your OpenAI API key")
            print()

        return False

    # Check configuration
    if not config.is_configured():
        print("❌ OpenAI API key not configured")
        print(f"📝 Please add OPENAI_API_KEY to {env_file}")
        return False

    print("✅ Configuration file: OK")

    # Test API connection
    print("🔍 Testing API connection...")
    if not test_api_connection():
        return False

    print("✅ API connection: OK")
    print()
    return True


def show_options():
    """Show available options to the user."""
    print("🎯 What would you like to do?")
    print()
    print("1. 🧪 Run API test")
    print("2. 🎭 Run demo (generate sample course)")
    print("3. 🚀 Interactive course generation")
    print("4. 📖 View documentation")
    print("5. ❌ Exit")
    print()


def run_option(choice):
    """Run the selected option."""
    if choice == "1":
        print("Running API test...")
        from src.intelligent_photocopier.test_api import main as test_main

        test_main()

    elif choice == "2":
        print("Running demo...")
        from src.intelligent_photocopier.demo import demo_course_generation

        demo_course_generation()

    elif choice == "3":
        print("Starting interactive mode...")
        from src.intelligent_photocopier.main import IntelligentPhotocopier

        photocopier = IntelligentPhotocopier(str(project_root))
        photocopier.run_interactive()

    elif choice == "4":
        print("📖 Documentation:")
        print()
        print(
            "🔗 Project Repository: https://github.com/chengxin199/IS601_MidtermProject_Intelligent-Photocopier"
        )
        print("📄 README: Check the README.md file for detailed instructions")
        print(
            "📚 Course Template: See Lessons/A1-Defensive-Programming/ for the template structure"
        )
        print("⚙️  Configuration: Check .env.example for configuration options")
        print()

    elif choice == "5":
        print("👋 Goodbye!")
        return False

    else:
        print("❌ Invalid choice. Please try again.")

    return True


def main():
    """Main function."""
    print_banner()

    # Check setup
    if not check_setup():
        print("🚫 Setup incomplete. Please fix the issues above and try again.")
        return

    # Main loop
    while True:
        show_options()
        choice = input("Enter your choice (1-5): ").strip()
        print()

        if not run_option(choice):
            break

        print()
        continue_prompt = input("Press Enter to continue or 'q' to quit: ").strip().lower()
        if continue_prompt == "q":
            print("👋 Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
