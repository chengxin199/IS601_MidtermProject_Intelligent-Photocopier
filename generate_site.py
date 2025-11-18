#!/usr/bin/env python3
"""
Website generator script for Intelligent Photocopier courses.
Generates a static website from course markdown files using Eleventy.
"""

import subprocess
import sys
from pathlib import Path


def check_node_installed() -> bool:
    """Check if Node.js is installed."""
    try:
        subprocess.run(
            ["node", "--version"],
            check=True,
            capture_output=True,
            text=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def check_npm_installed() -> bool:
    """Check if npm is installed."""
    try:
        subprocess.run(
            ["npm", "--version"],
            check=True,
            capture_output=True,
            text=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def install_dependencies() -> bool:
    """Install npm dependencies."""
    print("📦 Installing dependencies...")
    try:
        subprocess.run(
            ["npm", "install"],
            check=True,
            cwd=Path(__file__).parent
        )
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False


def build_website() -> bool:
    """Build the static website using Eleventy."""
    print("🔨 Building website...")
    try:
        subprocess.run(
            ["npm", "run", "build"],
            check=True,
            cwd=Path(__file__).parent
        )
        print("✅ Website built successfully")
        print("📁 Output directory: _site/")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error building website: {e}")
        return False


def serve_website() -> None:
    """Start development server."""
    print("🚀 Starting development server...")
    print("📡 Website will be available at: http://localhost:8080")
    print("Press Ctrl+C to stop the server\n")
    try:
        subprocess.run(
            ["npm", "run", "serve"],
            cwd=Path(__file__).parent
        )
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting server: {e}")


def clean_output() -> bool:
    """Clean the output directory."""
    print("🧹 Cleaning output directory...")
    try:
        subprocess.run(
            ["npm", "run", "clean"],
            check=True,
            cwd=Path(__file__).parent
        )
        print("✅ Output directory cleaned")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error cleaning output: {e}")
        return False


def main() -> None:
    """Main function."""
    print("🌐 Intelligent Photocopier - Website Generator\n")

    # Check prerequisites
    if not check_node_installed():
        print("❌ Node.js is not installed. Please install Node.js first.")
        print("   Visit: https://nodejs.org/")
        sys.exit(1)

    if not check_npm_installed():
        print("❌ npm is not installed. Please install npm first.")
        sys.exit(1)

    # Check if node_modules exists
    node_modules = Path(__file__).parent / "node_modules"
    if not node_modules.exists():
        if not install_dependencies():
            sys.exit(1)

    # Parse command line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "build":
            if not build_website():
                sys.exit(1)
        elif command == "serve":
            serve_website()
        elif command == "clean":
            if not clean_output():
                sys.exit(1)
        elif command == "install":
            if not install_dependencies():
                sys.exit(1)
        else:
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  build   - Build the static website")
            print("  serve   - Start development server")
            print("  clean   - Clean output directory")
            print("  install - Install dependencies")
            sys.exit(1)
    else:
        # Default: build and serve
        if build_website():
            serve_website()
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
