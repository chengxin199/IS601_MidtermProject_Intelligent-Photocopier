"""
Tests for B2-performance-optimization-and-profiling practice exercises.

This file contains tests to validate the practice exercises
and guide students through the learning process.
"""

import pytest
from .practice_module import example_function, ExampleClass


class TestPracticeModule:
    """Test the practice module implementation."""

    def test_example_function(self):
        """Test the example function."""
        # TODO: Add meaningful tests based on course objectives
        assert example_function() is not None

    def test_example_class(self):
        """Test the example class."""
        example = ExampleClass()
        assert example is not None

        # TODO: Add tests for class methods
        result = example.example_method()
        assert result is not None


# TODO: AI will generate course-specific test cases
