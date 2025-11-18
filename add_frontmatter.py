#!/usr/bin/env python3
"""Add front matter to old course markdown files."""

from pathlib import Path
from datetime import datetime

files_to_update = [
    # A1 files
    ("Lessons/A1-Defensive-Programming-Template/lesson-content.md", 
     "Defensive Programming - Detailed Lessons", "layouts/base.njk", ["lesson", "content"]),
    ("Lessons/A1-Defensive-Programming-Template/summary.md",
     "Defensive Programming - Summary", "layouts/base.njk", ["summary"]),
    ("Lessons/A1-Defensive-Programming-Template/reference/best_practices.md",
     "Defensive Programming - Best Practices", "layouts/base.njk", ["reference", "best-practices"]),
    ("Lessons/A1-Defensive-Programming-Template/reference/common_pitfalls.md",
     "Defensive Programming - Common Pitfalls", "layouts/base.njk", ["reference"]),
    ("Lessons/A1-Defensive-Programming-Template/reference/exercise_instructions.md",
     "Defensive Programming - Exercise Instructions", "layouts/base.njk", ["exercises"]),
    ("Lessons/A1-Defensive-Programming-Template/reference/python_exceptions.md",
     "Defensive Programming - Python Exceptions", "layouts/base.njk", ["reference"]),
    ("Lessons/A1-Defensive-Programming-Template/reference/quick_reference.md",
     "Defensive Programming - Quick Reference", "layouts/base.njk", ["reference", "quick-guide"]),
    ("Lessons/A1-Defensive-Programming-Template/solutions/calculator_solution.md",
     "Defensive Programming - Solution", "layouts/base.njk", ["solutions", "code"]),
    
    # C6 files
    ("Lessons/C6-working-with-thirdparty-libraries/lesson-content.md",
     "Third-Party Libraries - Detailed Lessons", "layouts/base.njk", ["lesson", "content"]),
    ("Lessons/C6-working-with-thirdparty-libraries/summary.md",
     "Third-Party Libraries - Summary", "layouts/base.njk", ["summary"]),
    ("Lessons/C6-working-with-thirdparty-libraries/reference/best_practices.md",
     "Third-Party Libraries - Best Practices", "layouts/base.njk", ["reference", "best-practices"]),
    ("Lessons/C6-working-with-thirdparty-libraries/reference/exercise_instructions.md",
     "Third-Party Libraries - Exercise Instructions", "layouts/base.njk", ["exercises"]),
    ("Lessons/C6-working-with-thirdparty-libraries/reference/quick_reference.md",
     "Third-Party Libraries - Quick Reference", "layouts/base.njk", ["reference", "quick-guide"]),
    ("Lessons/C6-working-with-thirdparty-libraries/solutions/practice_solution.md",
     "Third-Party Libraries - Solution", "layouts/base.njk", ["solutions", "code"]),
]

for file_path, title, layout, tags in files_to_update:
    path = Path(file_path)
    if not path.exists():
        print(f"⚠️  File not found: {file_path}")
        continue
    
    content = path.read_text()
    
    # Check if already has front matter
    if content.startswith("---"):
        print(f"✓ Already has front matter: {file_path}")
        continue
    
    # Create front matter
    tags_yaml = "\n".join([f"  - {tag}" for tag in tags])
    front_matter = f"""---
title: {title}
layout: {layout}
tags:
{tags_yaml}
date: {datetime.now().isoformat()}
---
"""
    
    # Add front matter
    new_content = front_matter + content
    path.write_text(new_content)
    print(f"✅ Added front matter: {file_path}")

print("\n🎉 Done!")
