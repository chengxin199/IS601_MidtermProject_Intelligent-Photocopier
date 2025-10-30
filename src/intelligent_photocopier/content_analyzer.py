"""
Content Analyzer - Extracts course information from user input.

This module analyzes user-provided course descriptions and extracts
key information like course title, objectives, and requirements.
"""

import re
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class CourseInfo:
    """Structured information about a course."""
    course_id: str
    title: str
    description: str
    objectives: List[str]
    duration: str
    level: str
    topics: List[str]
    prerequisites: List[str]


class ContentAnalyzer:
    """Analyzes user input to extract course information."""

    def __init__(self):
        self.course_counter = self._get_next_course_number()

    def _get_next_course_number(self) -> str:
        """Determine the next available course number."""
        # TODO: Scan existing Lessons directory to find next available number
        # For now, default to B1
        return "B1"

    def extract_course_info(self, content: str) -> Dict[str, Any]:
        """Extract structured course information from user content."""
        course_info = {
            "course_id": self._extract_course_id(content),
            "title": self._extract_title(content),
            "description": self._extract_description(content),
            "objectives": self._extract_objectives(content),
            "duration": self._extract_duration(content),
            "level": self._extract_level(content),
            "topics": self._extract_topics(content),
            "prerequisites": self._extract_prerequisites(content)
        }

        return course_info

    def _extract_course_id(self, content: str) -> str:
        """Extract or generate course ID."""
        # Look for patterns like "B1:", "C2:", etc.
        course_id_match = re.search(r'([A-Z]\d+):', content)
        if course_id_match:
            return course_id_match.group(1)

        # Generate next available ID
        return self.course_counter

    def _extract_title(self, content: str) -> str:
        """Extract course title from content."""
        # Look for main heading patterns
        title_patterns = [
            r'#\s*([A-Z]\d+:?\s*)?(.+?)(?:\n|$)',  # # B1: Title
            r'##?\s*(.+?)(?:\n|$)',                # ## Title
            r'Course:\s*(.+?)(?:\n|$)',            # Course: Title
            r'Topic:\s*(.+?)(?:\n|$)',             # Topic: Title
        ]

        for pattern in title_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                # Get the last group (title without course ID)
                title = match.groups()[-1].strip()
                if title and len(title) > 3:  # Ensure meaningful title
                    return title

        return "Generated Course"

    def _extract_description(self, content: str) -> str:
        """Extract course description."""
        # Look for description patterns
        lines = content.split('\n')
        description_lines = []

        in_description = False
        for line in lines:
            line = line.strip()

            # Skip headers and empty lines for description start
            if not line or line.startswith('#'):
                if description_lines:  # Stop if we've started collecting
                    break
                continue

            # Stop at learning objectives or other sections
            if re.match(r'##?\s*(learning objectives|objectives|goals)', line, re.IGNORECASE):
                break

            # Collect description lines
            if not in_description and len(line) > 20:  # Start of substantial content
                in_description = True

            if in_description:
                description_lines.append(line)

        return ' '.join(description_lines[:3])  # First few sentences

    def _extract_objectives(self, content: str) -> List[str]:
        """Extract learning objectives from content."""
        objectives = []

        # Find objectives section
        obj_section_match = re.search(
            r'##?\s*(?:learning )?objectives?:?\s*\n(.*?)(?=\n##|\n#|\Z)',
            content,
            re.IGNORECASE | re.DOTALL
        )

        if obj_section_match:
            obj_content = obj_section_match.group(1)

            # Extract bullet points or numbered items
            bullet_patterns = [
                r'[-*+]\s*(.+)',      # - objective
                r'\d+\.\s*(.+)',      # 1. objective
                r'✅\s*(.+)',         # ✅ objective
                r'•\s*(.+)',          # • objective
            ]

            for pattern in bullet_patterns:
                matches = re.findall(pattern, obj_content, re.MULTILINE)
                if matches:
                    objectives.extend([obj.strip() for obj in matches])
                    break

        # Fallback: look for any bullet points in content
        if not objectives:
            bullet_matches = re.findall(r'[-*]\s*(.+)', content)
            objectives = [obj.strip() for obj in bullet_matches[:5]]  # Max 5

        return objectives or ["Master the core concepts", "Apply practical skills"]

    def _extract_duration(self, content: str) -> str:
        """Extract course duration."""
        duration_patterns = [
            r'Duration:?\s*(\d+[-–]\d+\s*hours?)',
            r'Time:?\s*(\d+[-–]\d+\s*hours?)',
            r'(\d+[-–]\d+\s*hours?)',
            r'Duration:?\s*(\d+\s*hours?)',
        ]

        for pattern in duration_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                return match.group(1)

        return "3-4 hours"  # Default

    def _extract_level(self, content: str) -> str:
        """Extract difficulty level."""
        level_patterns = [
            r'Level:?\s*(Beginner|Intermediate|Advanced)',
            r'Difficulty:?\s*(Beginner|Intermediate|Advanced)',
            r'\b(Beginner|Intermediate|Advanced)\b',
        ]

        for pattern in level_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                return match.group(1).title()

        return "Intermediate"  # Default

    def _extract_topics(self, content: str) -> List[str]:
        """Extract main topics covered."""
        # This is a simplified extraction
        # Could be enhanced with NLP for better topic detection
        topics = []

        # Look for topics in headers
        header_matches = re.findall(r'##?\s*(.+)', content)
        for header in header_matches:
            if not re.match(r'(objectives?|goals?|description)', header, re.IGNORECASE):
                topics.append(header.strip())

        return topics[:5]  # Limit to 5 main topics

    def _extract_prerequisites(self, content: str) -> List[str]:
        """Extract prerequisites from content."""
        prereq_patterns = [
            r'Prerequisites?:?\s*\n(.*?)(?=\n##|\n#|\Z)',
            r'Requirements?:?\s*\n(.*?)(?=\n##|\n#|\Z)',
        ]

        for pattern in prereq_patterns:
            match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
            if match:
                prereq_content = match.group(1)
                # Extract bullet points
                prereqs = re.findall(r'[-*]\s*(.+)', prereq_content)
                return [p.strip() for p in prereqs]

        return ["Python programming fundamentals", "Basic software development experience"]
