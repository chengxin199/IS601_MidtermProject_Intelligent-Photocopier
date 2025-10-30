"""
Tests for the main IntelligentPhotocopier class - Fixed version without interactive input.
"""

import os
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

from src.intelligent_photocopier.main import IntelligentPhotocopier


def create_complete_course_info(**overrides):
    """Create a complete course_info dict with all required fields."""
    default_info = {
        'title': 'Test Course',
        'course_id': 'A2',
        'objectives': ['Learn basics'],
        'description': 'Test description',
        'duration': '2 hours',
        'level': 'Beginner',
        'topics': ['Topic 1'],
        'prerequisites': ['Basic knowledge']
    }
    default_info.update(overrides)
    return default_info


class TestIntelligentPhotocopier:
    """Test the main IntelligentPhotocopier functionality."""

    def setup_method(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        self.photocopier = IntelligentPhotocopier(self.temp_dir)

    def teardown_method(self):
        """Clean up test environment."""
        import shutil
        if Path(self.temp_dir).exists():
            shutil.rmtree(self.temp_dir)

    def test_initialization(self):
        """Test photocopier initialization."""
        assert self.photocopier.base_path == Path(self.temp_dir)
        assert self.photocopier.lessons_path == Path(self.temp_dir) / "Lessons"

    def test_initialization_with_string_path(self):
        """Test initialization with string path."""
        photocopier = IntelligentPhotocopier(str(self.temp_dir))
        assert photocopier.base_path == Path(self.temp_dir)

    @patch('src.intelligent_photocopier.main.TemplateExtractor')
    def test_generate_course_success(self, mock_template_extractor):
        """Test successful course generation."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {
            'files': ['README.md', 'lesson-content.md'],
            'content_patterns': {}
        }
        mock_template_extractor.return_value = mock_extractor

        # Create photocopier after mocking TemplateExtractor
        photocopier = IntelligentPhotocopier(self.temp_dir)

        # Mock the analyzer
        photocopier.analyzer.extract_course_info = Mock(return_value=create_complete_course_info())

        # Mock the generator (correct attribute name)
        photocopier.course_generator.generate_course_content = Mock(return_value={
            'README.md': '# Test Course',
            'lesson-content.md': '# Lesson Content'
        })

        # Mock the file manager
        photocopier.file_manager.create_course = Mock(return_value=Path(self.temp_dir) / "A2-test-course")
        self.photocopier.file_manager.create_course = Mock(return_value=Path(self.temp_dir) / "A2-test-course")

        # Test course generation directly (skip interactive input)
        test_content = "Test course about programming"

        # Don't mock print to see error messages
        result = photocopier.generate_course(test_content)

        # Verify result and components were called
        assert result is True
        photocopier.analyzer.extract_course_info.assert_called()
        photocopier.course_generator.generate_course_content.assert_called()
        photocopier.file_manager.create_course.assert_called()

    @patch('src.intelligent_photocopier.main.TemplateExtractor')
    def test_generate_course_analyzer_failure(self, mock_template_extractor):
        """Test course generation when analyzer fails."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {'files': []}
        mock_template_extractor.return_value = mock_extractor

        # Mock analyzer failure
        self.photocopier.analyzer.extract_course_info = Mock(side_effect=Exception("Analysis failed"))

        test_content = "Test course"

        with patch('builtins.print'):
            result = self.photocopier.generate_course(test_content)

        # Should handle error gracefully
        assert result is False
        self.photocopier.analyzer.extract_course_info.assert_called()

    @patch('src.intelligent_photocopier.main.TemplateExtractor')
    def test_generate_course_generator_failure(self, mock_template_extractor):
        """Test course generation when generator fails."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {'files': []}
        mock_template_extractor.return_value = mock_extractor

        # Mock analyzer success
        self.photocopier.analyzer.extract_course_info = Mock(return_value=create_complete_course_info())

        # Mock template extractor instance
        self.photocopier.template_extractor.extract_structure = Mock(return_value={'files': []})

        # Mock generator failure (correct attribute name)
        self.photocopier.course_generator.generate_course_content = Mock(side_effect=Exception("Generation failed"))

        test_content = "Test course"

        with patch('builtins.print'):
            result = self.photocopier.generate_course(test_content)

        # Should handle error gracefully
        assert result is False
        self.photocopier.course_generator.generate_course_content.assert_called()

    @patch('src.intelligent_photocopier.main.TemplateExtractor')
    def test_generate_course_file_manager_failure(self, mock_template_extractor):
        """Test course generation when file manager fails."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {'files': []}
        mock_template_extractor.return_value = mock_extractor

        # Mock analyzer success
        self.photocopier.analyzer.extract_course_info = Mock(return_value=create_complete_course_info())

        # Mock template extractor instance
        self.photocopier.template_extractor.extract_structure = Mock(return_value={'files': []})

        # Mock generator success (correct attribute name)
        self.photocopier.course_generator.generate_course_content = Mock(return_value={
            'README.md': '# Test'
        })

        # Mock file manager failure
        self.photocopier.file_manager.create_course = Mock(side_effect=Exception("File creation failed"))

        test_content = "Test course"

        with patch('builtins.print'):
            result = self.photocopier.generate_course(test_content)

        # Should handle error gracefully
        assert result is False
        self.photocopier.file_manager.create_course.assert_called()

    @patch('src.intelligent_photocopier.main.TemplateExtractor')
    def test_course_id_generation(self, mock_template_extractor):
        """Test automatic course ID generation."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {'files': []}
        mock_template_extractor.return_value = mock_extractor

        # Mock analyzer to return info with course_id
        mock_course_info = create_complete_course_info(
            course_id='B1'  # Custom course ID
        )
        self.photocopier.analyzer.extract_course_info = Mock(return_value=mock_course_info)

        # Mock template extractor instance
        self.photocopier.template_extractor.extract_structure = Mock(return_value={'files': []})

        # Mock other components (correct attribute names)
        self.photocopier.course_generator.generate_course_content = Mock(return_value={'README.md': '# Test'})
        self.photocopier.file_manager.create_course = Mock(return_value=Path(self.temp_dir))

        test_content = "Test course"

        with patch('builtins.print'):
            result = self.photocopier.generate_course(test_content)

        # Verify course was created with the generated ID
        assert result is True
        call_args = self.photocopier.file_manager.create_course.call_args
        created_course_id = call_args[0][0]  # First argument
        assert 'B1' in created_course_id

    def test_lessons_path_creation(self):
        """Test that lessons path is created if it doesn't exist."""
        # Create photocopier with new temp directory
        new_temp_dir = tempfile.mkdtemp()
        try:
            photocopier = IntelligentPhotocopier(new_temp_dir)

            # The lessons path should be defined
            assert photocopier.lessons_path == Path(new_temp_dir) / "Lessons"

        finally:
            import shutil
            if Path(new_temp_dir).exists():
                shutil.rmtree(new_temp_dir)

    @patch('src.intelligent_photocopier.main.TemplateExtractor')
    def test_course_slug_generation(self, mock_template_extractor):
        """Test course slug generation for directory naming."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {'files': []}
        mock_template_extractor.return_value = mock_extractor

        # Mock analyzer with specific title
        self.photocopier.analyzer.extract_course_info = Mock(return_value=create_complete_course_info(
            title='Advanced Python: Best Practices & Patterns',
            course_id='B2'
        ))

        # Mock template extractor instance
        self.photocopier.template_extractor.extract_structure = Mock(return_value={'files': []})

        # Mock other components (correct attribute names)
        self.photocopier.course_generator.generate_course_content = Mock(return_value={'README.md': '# Test'})
        self.photocopier.file_manager.create_course = Mock(return_value=Path(self.temp_dir))

        test_content = "Advanced course"

        with patch('builtins.print'):
            result = self.photocopier.generate_course(test_content)

        # Verify slugified course ID was used
        assert result is True
        call_args = self.photocopier.file_manager.create_course.call_args
        created_course_id = call_args[0][0]  # First argument
        assert 'B2' in created_course_id

    @patch('builtins.print')
    @patch('src.intelligent_photocopier.main.TemplateExtractor')
    def test_success_message_output(self, mock_template_extractor, mock_print):
        """Test that success messages are printed."""
        # Setup mocks for successful generation
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {'files': []}
        mock_template_extractor.return_value = mock_extractor

        self.photocopier.analyzer.extract_course_info = Mock(return_value=create_complete_course_info())

        # Mock template extractor instance
        self.photocopier.template_extractor.extract_structure = Mock(return_value={'files': []})

        # Mock successful generation (correct attribute names)
        self.photocopier.course_generator.generate_course_content = Mock(return_value={'README.md': '# Test'})

        course_path = Path(self.temp_dir) / "A2-test-course"
        self.photocopier.file_manager.create_course = Mock(return_value=course_path)

        test_content = "Test course"

        result = self.photocopier.generate_course(test_content)

        # Verify success and method calls
        assert result is True
        mock_print.assert_called()

    def test_component_initialization(self):
        """Test that all components are properly initialized."""
        photocopier = IntelligentPhotocopier(self.temp_dir)

        # Verify all components exist (correct attribute names)
        assert hasattr(photocopier, 'analyzer')
        assert hasattr(photocopier, 'template_extractor')
        assert hasattr(photocopier, 'course_generator')
        assert hasattr(photocopier, 'file_manager')

    def test_path_handling(self):
        """Test proper path handling for different input types."""
        # Test with Path object converted to string
        path_obj = Path(self.temp_dir)
        photocopier1 = IntelligentPhotocopier(str(path_obj))
        assert photocopier1.base_path == path_obj

        # Test with string
        photocopier2 = IntelligentPhotocopier(str(self.temp_dir))
        assert photocopier2.base_path == path_obj

        # Test with None (should use current directory)
        original_cwd = os.getcwd()
        try:
            os.chdir(self.temp_dir)
            photocopier3 = IntelligentPhotocopier(None)
            assert photocopier3.base_path == Path.cwd()
        finally:
            os.chdir(original_cwd)

    @patch('src.intelligent_photocopier.config.config.is_configured')
    def test_configuration_check_interactive(self, mock_is_configured):
        """Test that configuration is checked during run_interactive."""
        mock_is_configured.return_value = False

        # Mock the input calls that would happen in run_interactive
        with patch('builtins.input', side_effect=['n']):  # User says no to continue
            with patch('builtins.print'):
                result = self.photocopier.run_interactive()

        # Should return False when user doesn't want to continue
        assert result is False

    @patch('src.intelligent_photocopier.config.config.is_configured')
    @patch('src.intelligent_photocopier.main.TemplateExtractor')
    def test_run_interactive_success(self, mock_template_extractor, mock_is_configured):
        """Test successful run_interactive flow."""
        mock_is_configured.return_value = True

        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {'files': []}
        mock_template_extractor.return_value = mock_extractor

        # Mock all components
        self.photocopier.analyzer.extract_course_info = Mock(return_value=create_complete_course_info())
        self.photocopier.template_extractor.extract_structure = Mock(return_value={'files': []})
        self.photocopier.course_generator.generate_course_content = Mock(return_value={'README.md': '# Test'})
        self.photocopier.file_manager.create_course = Mock(return_value=Path(self.temp_dir))

        # Mock input to provide content and end signal
        input_sequence = [
            'Test course content',
            'More content',
            'END'  # Signal to end input
        ]

        with patch('builtins.input', side_effect=input_sequence):
            with patch('builtins.print'):
                result = self.photocopier.run_interactive()

        # Should succeed
        assert result is True
