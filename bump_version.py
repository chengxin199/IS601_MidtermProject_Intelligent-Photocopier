#!/usr/bin/env python3
"""
Version bump utility for Intelligent Photocopier.

Usage:
    python bump_version.py patch   # 1.0.0 -> 1.0.1
    python bump_version.py minor   # 1.0.0 -> 1.1.0
    python bump_version.py major   # 1.0.0 -> 2.0.0
"""

import argparse
import re
from datetime import datetime
from pathlib import Path


def read_version():
    """Read current version from VERSION file."""
    version_file = Path("VERSION")
    if not version_file.exists():
        return "1.0.0"
    return version_file.read_text().strip()


def write_version(version, quiet=False):
    """Write version to VERSION file."""
    version_file = Path("VERSION")
    version_file.write_text(version + "\n")
    if not quiet:
        print(f"✅ Updated VERSION file to {version}")


def bump_version(current, bump_type):
    """Bump version number."""
    major, minor, patch = map(int, current.split("."))

    if bump_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "minor":
        minor += 1
        patch = 0
    elif bump_type == "patch":
        patch += 1
    else:
        raise ValueError(f"Invalid bump type: {bump_type}")

    return f"{major}.{minor}.{patch}"


def update_index_njk(version, quiet=False):
    """Update version in Lessons/index.njk."""
    index_file = Path("Lessons/index.njk")
    if not index_file.exists():
        if not quiet:
            print("⚠️  Lessons/index.njk not found")
        return

    content = index_file.read_text()

    # Update version number
    content = re.sub(
        r'<span style="font-weight: 600; color: #4a5568;">v[\d.]+</span>',
        f'<span style="font-weight: 600; color: #4a5568;">v{version}</span>',
        content,
    )

    # Update last updated date
    today = datetime.now().strftime("%B %d, %Y")
    content = re.sub(
        r"Last updated: [A-Za-z]+ \d+, \d{4}",
        f"Last updated: {today}",
        content,
    )

    index_file.write_text(content)
    if not quiet:
        print(f"✅ Updated Lessons/index.njk to v{version}")


def main():
    parser = argparse.ArgumentParser(description="Bump version number")
    parser.add_argument(
        "bump_type",
        choices=["major", "minor", "patch"],
        help="Type of version bump",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress output messages (for automation)",
    )

    args = parser.parse_args()

    current_version = read_version()
    new_version = bump_version(current_version, args.bump_type)

    if not args.quiet:
        print(f"\n📦 Version Bump: {current_version} → {new_version}\n")

    if args.dry_run:
        print("🔍 DRY RUN - No files will be modified")
        print(f"   Would update VERSION file to: {new_version}")
        print(f"   Would update Lessons/index.njk to: v{new_version}")
        return

    # Update files
    write_version(new_version, quiet=args.quiet)
    update_index_njk(new_version, quiet=args.quiet)

    if not args.quiet:
        print("\n✨ Version bumped successfully!")
        print("\n📝 Next steps:")
        print("   git add VERSION Lessons/index.njk")
        print(f'   git commit -m "chore: Bump version to {new_version}"')
        print("   git push origin main")


if __name__ == "__main__":
    main()
