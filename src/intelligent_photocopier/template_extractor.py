"""
Template Extractor - Analyzes and extracts structure from existing courses.

This module examines the A1-Defensive-Programming course to understand
its structure, format, and patterns for replication.
"""

import os
from pathlib import Path
from typing import Any, Dict, List


class TemplateExtractor:
    """Extracts template structure from existing course content."""

    def __init__(self, template_path: Path):
        """Initialize with path to template course (A1-Defensive-Programming)."""
        self.template_path = Path(template_path)
        self.structure: Dict[str, Any] = {}

    def extract_structure(self) -> Dict[str, Any]:
        """Extract the complete structure of the template course."""
        if not self.template_path.exists():
            raise FileNotFoundError(f"Template course not found at {self.template_path}")

        structure = {
            "course_id": self.template_path.name,
            "files": self._extract_file_structure(),
            "content_patterns": self._extract_content_patterns(),
            "formatting_style": self._extract_formatting_style(),
            "navigation_structure": self._extract_navigation_structure(),
        }

        return structure

    def _extract_file_structure(self) -> Dict[str, Any]:
        """Extract the file and folder structure."""
        structure: Dict[str, Any] = {"directories": [], "files": {}}

        for root, _dirs, files in os.walk(self.template_path):
            rel_path = Path(root).relative_to(self.template_path)

            # Track directories
            if rel_path != Path("."):
                structure["directories"].append(str(rel_path))

            # Track files with their relative paths
            for file in files:
                if file.endswith((".md", ".py")):
                    file_path = rel_path / file if rel_path != Path(".") else Path(file)
                    structure["files"][str(file_path)] = {
                        "type": "markdown" if file.endswith(".md") else "python",
                        "size": (Path(root) / file).stat().st_size,
                        "purpose": self._infer_file_purpose(file),
                    }

        return structure

    def _extract_content_patterns(self) -> Dict[str, Any]:
        """Extract content patterns from key files."""
        patterns = {}

        key_files = {
            "README.md": "overview_pattern",
            "lesson-content.md": "lesson_pattern",
            "summary.md": "summary_pattern",
        }

        for filename, pattern_name in key_files.items():
            file_path = self.template_path / filename
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    patterns[pattern_name] = self._analyze_content_structure(content)

        return patterns

    def _extract_formatting_style(self) -> Dict[str, Any]:
        """Extract formatting and style patterns."""
        readme_path = self.template_path / "README.md"
        if not readme_path.exists():
            return {}

        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        style = {
            "emoji_usage": self._extract_emoji_patterns(content),
            "header_style": self._extract_header_patterns(content),
            "list_formatting": self._extract_list_patterns(content),
            "code_block_style": self._extract_code_patterns(content),
            "emphasis_style": self._extract_emphasis_patterns(content),
        }

        return style

    def _extract_navigation_structure(self) -> Dict[str, Any]:
        """Extract navigation and linking patterns."""
        readme_path = self.template_path / "README.md"
        if not readme_path.exists():
            return {}

        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        import re

        # Extract internal links
        internal_links = re.findall(r"\[([^\]]+)\]\(([^)]+\.md[^)]*)\)", content)

        # Extract section structure
        headers = re.findall(r"^(#+)\s*(.+)$", content, re.MULTILINE)

        navigation = {
            "internal_links": internal_links,
            "section_hierarchy": headers,
            "folder_structure_links": self._extract_folder_links(content),
        }

        return navigation

    def _infer_file_purpose(self, filename: str) -> str:
        """Infer the purpose of a file based on its name."""
        purpose_map = {
            "README.md": "course_overview",
            "lesson-content.md": "main_lesson",
            "summary.md": "lesson_summary",
            "calculator.py": "practice_module",
            "config_loader.py": "practice_module",
            "test_": "test_file",
            "_hardened.py": "reference_implementation",
            "exercise_instructions.md": "exercise_guide",
            "best_practices.md": "reference_material",
            "quick_reference.md": "reference_material",
            "common_pitfalls.md": "reference_material",
        }

        for key, purpose in purpose_map.items():
            if key in filename:
                return purpose

        return "unknown"

    def _analyze_content_structure(self, content: str) -> Dict[str, Any]:
        """Analyze the structure of content."""
        import re

        # Count sections
        headers = re.findall(r"^(#+)\s*(.+)$", content, re.MULTILINE)

        # Extract code blocks
        code_blocks = re.findall(r"```(\w+)?\n(.*?)```", content, re.DOTALL)

        # Extract lists
        bullet_lists = re.findall(r"^[-*+]\s+(.+)$", content, re.MULTILINE)
        numbered_lists = re.findall(r"^\d+\.\s+(.+)$", content, re.MULTILINE)

        structure = {
            "header_count": len(headers),
            "max_header_level": max((len(h[0]) for h in headers), default=0),
            "code_block_count": len(code_blocks),
            "code_languages": list({cb[0] for cb in code_blocks if cb[0]}),
            "bullet_list_items": len(bullet_lists),
            "numbered_list_items": len(numbered_lists),
            "content_length": len(content),
            "paragraph_count": len([p for p in content.split("\n\n") if p.strip()]),
        }

        return structure

    def _extract_emoji_patterns(self, content: str) -> List[str]:
        """Extract emoji usage patterns."""
        import re

        emojis = re.findall(r"([🌟🎯📚🛡️🚀⚡💻🔧🆘🎮🏗️📈🎓💡🔍📊📖✅❌🤖📋🧪])", content)
        return list(set(emojis))

    def _extract_header_patterns(self, content: str) -> List[str]:
        """Extract header formatting patterns."""
        import re

        headers = re.findall(r"^(#+\s*.+)$", content, re.MULTILINE)
        return headers[:10]  # Sample of headers

    def _extract_list_patterns(self, content: str) -> Dict[str, List[str]]:
        """Extract list formatting patterns."""
        import re

        bullet_patterns = re.findall(r"^([-*+✅❌]\s+.+)$", content, re.MULTILINE)
        numbered_patterns = re.findall(r"^(\d+\.\s+.+)$", content, re.MULTILINE)

        return {"bullet_examples": bullet_patterns[:5], "numbered_examples": numbered_patterns[:5]}

    def _extract_code_patterns(self, content: str) -> List[str]:
        """Extract code block patterns."""
        import re

        code_blocks = re.findall(r"```(\w+)?\n(.*?)```", content, re.DOTALL)
        return [f"```{lang}" for lang, _ in code_blocks if lang][:5]

    def _extract_emphasis_patterns(self, content: str) -> List[str]:
        """Extract emphasis and formatting patterns."""
        import re

        patterns = []
        patterns.extend(re.findall(r"\*\*([^*]+)\*\*", content)[:3])  # Bold
        patterns.extend(re.findall(r"`([^`]+)`", content)[:3])  # Code
        patterns.extend(re.findall(r"_([^_]+)_", content)[:3])  # Italic

        return patterns

    def _extract_folder_links(self, content: str) -> List[str]:
        """Extract folder structure representations."""
        import re

        # Look for ASCII folder trees
        tree_lines = re.findall(r"^[├└│\s]*[├└]─+\s*(.+)$", content, re.MULTILINE)
        return tree_lines[:10]  # Sample of folder structure lines
