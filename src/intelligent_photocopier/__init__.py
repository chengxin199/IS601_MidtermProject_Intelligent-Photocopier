"""
Intelligent Photocopier - AI-Powered Course Generation Tool

This module provides functionality to automatically generate educational course content
based on existing templates, using AI to create contextually appropriate materials.
"""

__version__ = "0.1.0"
__author__ = "Course Generator Team"

from .content_analyzer import ContentAnalyzer
from .course_generator import CourseGenerator
from .file_manager import FileManager
from .template_extractor import TemplateExtractor

__all__ = ["ContentAnalyzer", "TemplateExtractor", "CourseGenerator", "FileManager"]
