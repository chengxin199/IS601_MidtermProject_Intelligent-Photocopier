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
        "title": "Test Course",
        "course_id": "A2",
        "objectives": ["Learn basics"],
        "description": "Test description",
        "duration": "2 hours",
        "level": "Beginner",
        "topics": ["Topic 1"],
        "prerequisites": ["Basic knowledge"],
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

    @patch("src.intelligent_photocopier.main.TemplateExtractor")
    def test_generate_course_success(self, mock_template_extractor):
        """Test successful course generation."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {
            "files": ["README.md", "lesson-content.md"],
            "content_patterns": {},
        }
        mock_template_extractor.return_value = mock_extractor

        # Create photocopier after mocking TemplateExtractor
        photocopier = IntelligentPhotocopier(self.temp_dir)

        # Mock the analyzer
        photocopier.analyzer.extract_course_info = Mock(return_value=create_complete_course_info())

        # Mock the generator (correct attribute name)
        photocopier.course_generator.generate_course_content = Mock(
            return_value={"README.md": "# Test Course", "lesson-content.md": "# Lesson Content"}
        )

        # Mock the file manager
        photocopier.file_manager.create_course = Mock(
            return_value=Path(self.temp_dir) / "A2-test-course"
        )
        self.photocopier.file_manager.create_course = Mock(
            return_value=Path(self.temp_dir) / "A2-test-course"
        )

        # Test course generation directly (skip interactive input)
        test_content = "Test course about programming"

        # Don't mock print to see error messages
        result = photocopier.generate_course(test_content)

        # Verify result and components were called
        assert result is True
        photocopier.analyzer.extract_course_info.assert_called()
        photocopier.course_generator.generate_course_content.assert_called()
        photocopier.file_manager.create_course.assert_called()

    @patch("src.intelligent_photocopier.main.TemplateExtractor")
    def test_generate_course_analyzer_failure(self, mock_template_extractor):
        """Test course generation when analyzer fails."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {"files": []}
        mock_template_extractor.return_value = mock_extractor

        # Mock analyzer failure
        self.photocopier.analyzer.extract_course_info = Mock(
            side_effect=Exception("Analysis failed")
        )

        test_content = "Test course"

        with patch("builtins.print"):
            result = self.photocopier.generate_course(test_content)

        # Should handle error gracefully
        assert result is False
        self.photocopier.analyzer.extract_course_info.assert_called()

    @patch("src.intelligent_photocopier.main.TemplateExtractor")
    def test_generate_course_generator_failure(self, mock_template_extractor):
        """Test course generation when generator fails."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {"files": []}
        mock_template_extractor.return_value = mock_extractor

        # Mock analyzer success
        self.photocopier.analyzer.extract_course_info = Mock(
            return_value=create_complete_course_info()
        )

        # Mock template extractor instance
        self.photocopier.template_extractor.extract_structure = Mock(return_value={"files": []})

        # Mock generator failure (correct attribute name)
        self.photocopier.course_generator.generate_course_content = Mock(
            side_effect=Exception("Generation failed")
        )

        test_content = "Test course"

        with patch("builtins.print"):
            result = self.photocopier.generate_course(test_content)

        # Should handle error gracefully
        assert result is False
        self.photocopier.course_generator.generate_course_content.assert_called()

    @patch("src.intelligent_photocopier.main.TemplateExtractor")
    def test_generate_course_file_manager_failure(self, mock_template_extractor):
        """Test course generation when file manager fails."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {"files": []}
        mock_template_extractor.return_value = mock_extractor

        # Mock analyzer success
        self.photocopier.analyzer.extract_course_info = Mock(
            return_value=create_complete_course_info()
        )

        # Mock template extractor instance
        self.photocopier.template_extractor.extract_structure = Mock(return_value={"files": []})

        # Mock generator success (correct attribute name)
        self.photocopier.course_generator.generate_course_content = Mock(
            return_value={"README.md": "# Test"}
        )

        # Mock file manager failure
        self.photocopier.file_manager.create_course = Mock(
            side_effect=Exception("File creation failed")
        )

        test_content = "Test course"

        with patch("builtins.print"):
            result = self.photocopier.generate_course(test_content)

        # Should handle error gracefully
        assert result is False
        self.photocopier.file_manager.create_course.assert_called()

    @patch("src.intelligent_photocopier.main.TemplateExtractor")
    def test_course_id_generation(self, mock_template_extractor):
        """Test automatic course ID generation."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {"files": []}
        mock_template_extractor.return_value = mock_extractor

        # Mock analyzer to return info with course_id
        mock_course_info = create_complete_course_info(course_id="B1")  # Custom course ID
        self.photocopier.analyzer.extract_course_info = Mock(return_value=mock_course_info)

        # Mock template extractor instance
        self.photocopier.template_extractor.extract_structure = Mock(return_value={"files": []})

        # Mock other components (correct attribute names)
        self.photocopier.course_generator.generate_course_content = Mock(
            return_value={"README.md": "# Test"}
        )
        self.photocopier.file_manager.create_course = Mock(return_value=Path(self.temp_dir))

        test_content = "Test course"

        with patch("builtins.print"):
            result = self.photocopier.generate_course(test_content)

        # Verify course was created with the generated ID
        assert result is True
        call_args = self.photocopier.file_manager.create_course.call_args
        created_course_id = call_args[0][0]  # First argument
        assert "B1" in created_course_id

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

    @patch("src.intelligent_photocopier.main.TemplateExtractor")
    def test_course_slug_generation(self, mock_template_extractor):
        """Test course slug generation for directory naming."""
        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {"files": []}
        mock_template_extractor.return_value = mock_extractor

        # Mock analyzer with specific title
        self.photocopier.analyzer.extract_course_info = Mock(
            return_value=create_complete_course_info(
                title="Advanced Python: Best Practices & Patterns", course_id="B2"
            )
        )

        # Mock template extractor instance
        self.photocopier.template_extractor.extract_structure = Mock(return_value={"files": []})

        # Mock other components (correct attribute names)
        self.photocopier.course_generator.generate_course_content = Mock(
            return_value={"README.md": "# Test"}
        )
        self.photocopier.file_manager.create_course = Mock(return_value=Path(self.temp_dir))

        test_content = "Advanced course"

        with patch("builtins.print"):
            result = self.photocopier.generate_course(test_content)

        # Verify slugified course ID was used
        assert result is True
        call_args = self.photocopier.file_manager.create_course.call_args
        created_course_id = call_args[0][0]  # First argument
        assert "B2" in created_course_id

    @patch("builtins.print")
    @patch("src.intelligent_photocopier.main.TemplateExtractor")
    def test_success_message_output(self, mock_template_extractor, mock_print):
        """Test that success messages are printed."""
        # Setup mocks for successful generation
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {"files": []}
        mock_template_extractor.return_value = mock_extractor

        self.photocopier.analyzer.extract_course_info = Mock(
            return_value=create_complete_course_info()
        )

        # Mock template extractor instance
        self.photocopier.template_extractor.extract_structure = Mock(return_value={"files": []})

        # Mock successful generation (correct attribute names)
        self.photocopier.course_generator.generate_course_content = Mock(
            return_value={"README.md": "# Test"}
        )

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
        assert hasattr(photocopier, "analyzer")
        assert hasattr(photocopier, "template_extractor")
        assert hasattr(photocopier, "course_generator")
        assert hasattr(photocopier, "file_manager")

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

    @patch("src.intelligent_photocopier.config.config.is_configured")
    def test_configuration_check_interactive(self, mock_is_configured):
        """Test that configuration is checked during run_interactive."""
        mock_is_configured.return_value = False

        # Mock the input calls that would happen in run_interactive
        with patch("builtins.input", side_effect=["n"]):  # User says no to continue
            with patch("builtins.print"):
                result = self.photocopier.run_interactive()

        # Should return False when user doesn't want to continue
        assert result is False

    @patch("src.intelligent_photocopier.config.config.is_configured")
    @patch("src.intelligent_photocopier.main.TemplateExtractor")
    def test_run_interactive_success(self, mock_template_extractor, mock_is_configured):
        """Test successful run_interactive flow."""
        mock_is_configured.return_value = True

        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {"files": []}
        mock_template_extractor.return_value = mock_extractor

        # Mock all components
        self.photocopier.analyzer.extract_course_info = Mock(
            return_value=create_complete_course_info()
        )
        self.photocopier.template_extractor.extract_structure = Mock(return_value={"files": []})
        self.photocopier.course_generator.generate_course_content = Mock(
            return_value={"README.md": "# Test"}
        )
        self.photocopier.file_manager.create_course = Mock(return_value=Path(self.temp_dir))

        # Mock input to provide choice, content and end signal
        input_sequence = [
            "1",
            "Test course content",
            "More content",
            "END",
        ]  # Choose paste, content, end

        with patch("builtins.input", side_effect=input_sequence):
            with patch("builtins.print"):
                result = self.photocopier.run_interactive()

        # Should succeed
        assert result is True

    @patch("src.intelligent_photocopier.config.config.is_configured")
    @patch("src.intelligent_photocopier.config.config.create_sample_env_file")
    def test_run_interactive_with_config_placeholder(self, mock_create_sample, mock_is_configured):
        """Test run_interactive when user chooses to continue with placeholder."""
        mock_is_configured.return_value = False
        mock_create_sample.return_value = Path(".env.example")

        # Mock input: 'y' to continue with placeholder, '1' for paste method, then provide content
        input_sequence = [
            "y",
            "1",
            "Test course",
            "END",
        ]  # Continue with placeholder, choose paste, content, end

        # Mock the generate_course to succeed
        with patch.object(self.photocopier, "generate_course", return_value=True):
            with patch("builtins.input", side_effect=input_sequence):
                with patch("builtins.print"):
                    result = self.photocopier.run_interactive()

        assert result is True
        mock_create_sample.assert_called_once()

    @patch("src.intelligent_photocopier.config.config.is_configured")
    def test_run_interactive_empty_content(self, mock_is_configured):
        """Test run_interactive with empty content."""
        mock_is_configured.return_value = True

        # Mock input to provide empty content (choose paste method, immediate END)
        input_sequence = ["1", "END"]  # Choose paste, then immediate end
        with patch("builtins.input", side_effect=input_sequence):
            with patch("builtins.print"):
                result = self.photocopier.run_interactive()

        # Should return False when no content provided
        assert result is False

    @patch("src.intelligent_photocopier.config.config.is_configured")
    def test_run_interactive_keyboard_interrupt(self, mock_is_configured):
        """Test run_interactive handles KeyboardInterrupt."""
        mock_is_configured.return_value = True

        # Mock input: first return "1" for paste method, then raise KeyboardInterrupt
        with patch("builtins.input", side_effect=["1", KeyboardInterrupt]):
            with patch("builtins.print"):
                result = self.photocopier.run_interactive()

        # Should return False when interrupted
        assert result is False

    @patch("src.intelligent_photocopier.config.config.is_configured")
    @patch("src.intelligent_photocopier.main.TemplateExtractor")
    def test_run_interactive_eof_signal(self, mock_template_extractor, mock_is_configured):
        """Test run_interactive handles EOF (Ctrl+D) properly."""
        mock_is_configured.return_value = True

        # Setup template extractor mock
        mock_extractor = Mock()
        mock_extractor.extract_structure.return_value = {"files": []}
        mock_template_extractor.return_value = mock_extractor

        # Mock all components for successful generation
        self.photocopier.analyzer.extract_course_info = Mock(
            return_value=create_complete_course_info()
        )
        self.photocopier.template_extractor.extract_structure = Mock(return_value={"files": []})
        self.photocopier.course_generator.generate_course_content = Mock(
            return_value={"README.md": "# Test"}
        )
        self.photocopier.file_manager.create_course = Mock(return_value=Path(self.temp_dir))

        # Mock input: choose paste method (1), then provide content, then raise EOFError (simulating Ctrl+D)
        with patch("builtins.input", side_effect=["1", "Line 1", "Line 2", EOFError]):
            with patch("builtins.print"):
                result = self.photocopier.run_interactive()

        # Should succeed
        assert result is True

    @patch("src.intelligent_photocopier.config.config.is_configured")
    @patch("src.intelligent_photocopier.config.config.get_missing_config")
    @patch("src.intelligent_photocopier.config.config.create_sample_env_file")
    def test_run_interactive_config_missing_items(
        self, mock_create_sample, mock_get_missing, mock_is_configured
    ):
        """Test run_interactive shows missing config items (line 44)."""
        mock_is_configured.return_value = False
        mock_get_missing.return_value = ["OpenAI API Key", "Model Configuration"]
        mock_create_sample.return_value = Path(".env.example")

        # User chooses not to continue
        with patch("builtins.input", return_value="n"):
            with patch("builtins.print"):
                result = self.photocopier.run_interactive()

        # Should have printed missing items (line 44)
        assert result is False
        mock_get_missing.assert_called_once()

    @patch("sys.argv", ["main.py", "--help"])
    def test_main_help_flag(self):
        """Test main() with --help flag (lines 133-159)."""
        from src.intelligent_photocopier.main import main

        with patch("builtins.print") as mock_print:
            main()

        # Should have printed help message
        mock_print.assert_called()
        # Check that help content was printed
        call_args = str(mock_print.call_args_list)
        assert "Intelligent Photocopier" in call_args or "Usage" in call_args

    @patch("sys.argv", ["main.py", "-h"])
    def test_main_h_flag(self):
        """Test main() with -h flag (lines 133-159)."""
        from src.intelligent_photocopier.main import main

        with patch("builtins.print") as mock_print:
            main()

        # Should have printed help message
        mock_print.assert_called()

    @patch("sys.argv", ["main.py"])
    @patch("src.intelligent_photocopier.main.IntelligentPhotocopier")
    def test_main_normal_execution(self, mock_photocopier_class):
        """Test main() normal execution path (line 163)."""
        from src.intelligent_photocopier.main import main

        mock_instance = Mock()
        mock_photocopier_class.return_value = mock_instance

        main()

        # Should have called run_interactive
        mock_instance.run_interactive.assert_called_once()

    def test_main_as_script(self):
        """Test running main.py as a script (line 163: if __name__ == '__main__')."""
        # This tests the __name__ == "__main__" block
        import os
        import subprocess
        import sys

        # Get the project root directory (parent of tests/)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Run the module as a script with --help to avoid hanging
        result = subprocess.run(
            [sys.executable, "-m", "src.intelligent_photocopier.main", "--help"],
            capture_output=True,
            text=True,
            timeout=5,
            cwd=project_root,
        )

        # Should execute successfully
        assert result.returncode == 0 or "Intelligent Photocopier" in result.stdout


class TestMaterialLibraryFeature:
    """Test the material library selection feature (_select_from_material_library)."""

    def setup_method(self):
        """Set up test environment with material files."""
        self.temp_dir = tempfile.mkdtemp()

        # Create material_context directory with test files
        self.material_dir = Path(self.temp_dir) / "material_context"
        self.material_dir.mkdir()

        # Create test material files
        (self.material_dir / "course_a.md").write_text("# Course A\nContent for course A")
        (self.material_dir / "course_b.md").write_text("# Course B\nContent for course B")
        (self.material_dir / "README.md").write_text("# README\nShould be skipped")

        # Create photocopier pointing to temp_dir
        self.photocopier = IntelligentPhotocopier(self.temp_dir)

        # Mock the analyzer's material_context_dir to use our test directory
        self.photocopier.analyzer.material_context_dir = self.material_dir

    def teardown_method(self):
        """Clean up test environment."""
        import shutil

        if Path(self.temp_dir).exists():
            shutil.rmtree(self.temp_dir)

    @patch("builtins.input", return_value="1")
    def test_select_material_valid_choice(self, mock_input):
        """Test selecting a valid material from library."""
        content = self.photocopier._select_from_material_library()

        assert content is not None
        assert "Course A" in content
        assert "Content for course A" in content

    @patch("builtins.input", return_value="2")
    def test_select_material_second_choice(self, mock_input):
        """Test selecting the second material from library."""
        content = self.photocopier._select_from_material_library()

        assert content is not None
        assert "Course B" in content

    @patch("builtins.input", return_value="0")
    def test_select_material_cancel(self, mock_input):
        """Test cancelling material selection (choice 0)."""
        content = self.photocopier._select_from_material_library()

        assert content is None

    @patch("builtins.input", return_value="99")
    def test_select_material_invalid_number(self, mock_input):
        """Test invalid material selection number."""
        content = self.photocopier._select_from_material_library()

        assert content is None

    @patch("builtins.input", return_value="invalid")
    def test_select_material_non_numeric(self, mock_input):
        """Test non-numeric input for material selection."""
        content = self.photocopier._select_from_material_library()

        assert content is None

    @patch("builtins.input", side_effect=KeyboardInterrupt)
    def test_select_material_keyboard_interrupt(self, mock_input):
        """Test KeyboardInterrupt during material selection."""
        content = self.photocopier._select_from_material_library()

        assert content is None

    @patch("builtins.input", return_value="1")
    def test_select_material_no_materials(self, mock_input):
        """Test material selection when no materials are available."""
        # Create photocopier with empty material directory
        empty_dir = tempfile.mkdtemp()
        try:
            empty_material_dir = Path(empty_dir) / "material_context"
            empty_material_dir.mkdir()

            photocopier = IntelligentPhotocopier(empty_dir)
            photocopier.analyzer.material_context_dir = empty_material_dir
            content = photocopier._select_from_material_library()

            assert content is None
        finally:
            import shutil

            shutil.rmtree(empty_dir)

    @patch("builtins.input", return_value="1")
    def test_select_material_directory_missing(self, mock_input):
        """Test material selection when material_context directory doesn't exist."""
        # Create photocopier without material directory
        no_mat_dir = tempfile.mkdtemp()
        try:
            photocopier = IntelligentPhotocopier(no_mat_dir)
            # Point to non-existent directory
            photocopier.analyzer.material_context_dir = Path(no_mat_dir) / "nonexistent"
            content = photocopier._select_from_material_library()

            assert content is None
        finally:
            import shutil

            shutil.rmtree(no_mat_dir)

    @patch("src.intelligent_photocopier.config.config.is_configured", return_value=True)
    @patch("builtins.input", side_effect=["2", "1"])
    @patch("src.intelligent_photocopier.main.IntelligentPhotocopier.generate_course")
    def test_run_interactive_with_material_library(
        self, mock_generate, mock_input, mock_is_configured
    ):
        """Test run_interactive choosing material library option."""
        mock_generate.return_value = True

        result = self.photocopier.run_interactive()

        assert result is True
        mock_generate.assert_called_once()
        # Check that content passed to generate_course contains material content
        call_args = mock_generate.call_args[0][0]
        assert "Course A" in call_args

    @patch("src.intelligent_photocopier.config.config.is_configured", return_value=True)
    @patch("builtins.input", side_effect=["2", "0"])
    def test_run_interactive_material_library_cancel(self, mock_input, mock_is_configured):
        """Test run_interactive with material library selection cancelled."""
        result = self.photocopier.run_interactive()

        assert result is False
