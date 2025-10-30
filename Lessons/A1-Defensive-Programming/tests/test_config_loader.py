"""
Tests for config_loader module - Practice for defensive programming.

🎯 YOUR TASK: Apply defensive programming principles to config_loader.py

This file contains basic tests for the configuration loader. Your job is to:

1. **Study the hardened example**: See test_config_loader_hardened.py for a complete
   implementation of defensive programming principles applied to configuration management.

2. **Improve config_loader.py**: Apply the following defensive programming techniques:
   - Add explicit pre-/post-condition checks and assertions where helpful
   - Replace ambiguous return codes with custom exceptions
   - Introduce guard clauses to simplify branching
   - Add logging at error boundaries with actionable context
   - Update tests to cover error scenarios and contracts

3. **Required improvements**:
   - Create custom exception hierarchy (ConfigError, ConfigFileError, ConfigValidationError)
   - Add comprehensive input validation with detailed error messages
   - Implement secure logging that redacts sensitive configuration data
   - Add guard clauses for file operations and validation
   - Replace generic error handling with specific exception types
   - Write tests for all error scenarios and edge cases

4. **Acceptance criteria**:
   - [ ] Tests pass and include error-path coverage (>= 2 new tests)
   - [ ] No bare except statements; custom exceptions used appropriately
   - [ ] Logs include context without leaking sensitive data (passwords, keys)
   - [ ] Configuration validation provides actionable error messages
   - [ ] File operations handle all error conditions gracefully

📚 **Reference the hardened implementation** in test_config_loader_hardened.py to see
how defensive programming principles are applied to configuration management.

💡 **Focus on security**: Pay special attention to logging - configuration files
often contain sensitive data that should never appear in logs.

🔍 **Key areas to harden**:
   - File loading and JSON parsing
   - Configuration validation and structure checking
   - Error handling and fallback mechanisms
   - Secure logging of configuration operations
"""

import pytest
import json
import os
import tempfile
import sys
from unittest.mock import patch, mock_open

# Add the tests directory to path so we can import config_loader
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config_loader import (
    load_config, validate_config, get_database_config, get_api_config,
    merge_configs, ConfigManager, create_sample_config
)


class TestLoadConfig:
    """Test configuration loading functionality."""

    def test_load_valid_config(self):
        """Test loading a valid JSON configuration file."""
        valid_config = {"key": "value", "number": 42}

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(valid_config, f)
            temp_filename = f.name

        try:
            config = load_config(temp_filename)
            assert config == valid_config
        finally:
            os.unlink(temp_filename)

    def test_load_nonexistent_file(self):
        """Test loading a non-existent file."""
        # TODO: Update when you implement proper exception handling
        with pytest.raises(FileNotFoundError):
            load_config("nonexistent_file.json")

    # TODO: Add test for invalid JSON
    # TODO: Add test for permission errors
    # TODO: Add test for empty files


class TestValidateConfig:
    """Test configuration validation."""

    def test_validate_complete_config(self):
        """Test validation of complete configuration."""
        valid_config = {
            "database": {"host": "localhost"},
            "api": {"base_url": "http://api.example.com"},
            "logging": {"level": "INFO"}
        }
        assert validate_config(valid_config) is True

    def test_validate_missing_required_keys(self):
        """Test validation fails for missing required keys."""
        invalid_config = {
            "database": {"host": "localhost"}
            # Missing 'api' and 'logging'
        }
        assert validate_config(invalid_config) is False

    # TODO: Add more comprehensive validation tests
    # TODO: Add tests for invalid value types
    # TODO: Add tests for invalid value ranges


class TestConfigExtraction:
    """Test configuration extraction functions."""

    def test_get_database_config(self):
        """Test extracting database configuration."""
        config = {
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "testdb",
                "user": "testuser",
                "password": "testpass"
            }
        }

        db_config = get_database_config(config)
        assert db_config["host"] == "localhost"
        assert db_config["port"] == 5432

    def test_get_api_config(self):
        """Test extracting API configuration."""
        config = {
            "api": {
                "base_url": "https://api.example.com",
                "timeout": 30,
                "retry_attempts": 3,
                "api_key": "secret"
            }
        }

        api_config = get_api_config(config)
        assert api_config["base_url"] == "https://api.example.com"
        assert api_config["timeout"] == 30

    # TODO: Add tests for missing keys
    # TODO: Add tests for invalid data types
    # TODO: Add tests for missing optional keys


class TestMergeConfigs:
    """Test configuration merging."""

    def test_merge_simple_configs(self):
        """Test merging simple configurations."""
        default = {"a": 1, "b": 2}
        user = {"b": 3, "c": 4}

        merged = merge_configs(default, user)
        assert merged == {"a": 1, "b": 3, "c": 4}

    # TODO: Add tests for nested configuration merging
    # TODO: Add tests for conflicting data types
    # TODO: Add tests for deep merging


class TestConfigManager:
    """Test the ConfigManager class."""

    def test_config_manager_initialization(self):
        """Test ConfigManager initializes correctly."""
        manager = ConfigManager("test.json")
        assert manager.config_file == "test.json"
        assert manager.config == {}

    def test_load_existing_file(self):
        """Test loading existing configuration file."""
        config_data = {
            "database": {"host": "localhost", "port": 5432, "name": "test", "user": "user", "password": "pass"},
            "api": {"base_url": "http://api.test.com", "timeout": 30, "retry_attempts": 3},
            "logging": {"level": "DEBUG"}
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(config_data, f)
            temp_filename = f.name

        try:
            manager = ConfigManager(temp_filename)
            manager.load()
            # Should be merged with defaults
            assert "database" in manager.config
            assert manager.config["database"]["host"] == "localhost"
        finally:
            os.unlink(temp_filename)

    def test_load_nonexistent_file_uses_defaults(self):
        """Test loading non-existent file falls back to defaults."""
        manager = ConfigManager("nonexistent.json")
        manager.load()

        # Should use default configuration
        assert manager.config == manager.default_config

    def test_get_configuration_value(self):
        """Test getting configuration values."""
        manager = ConfigManager()
        manager.config = {"test_key": "test_value"}

        assert manager.get("test_key") == "test_value"
        assert manager.get("missing_key", "default") == "default"

    def test_get_database_url(self):
        """Test generating database URL."""
        manager = ConfigManager()
        manager.config = {
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "testdb",
                "user": "testuser",
                "password": "testpass"
            }
        }

        url = manager.get_database_url()
        expected = "postgresql://testuser:testpass@localhost:5432/testdb"
        assert url == expected

    # TODO: Add tests for save functionality
    # TODO: Add tests for reload functionality
    # TODO: Add tests for error handling in all methods


class TestCreateSampleConfig:
    """Test sample configuration creation."""

    def test_create_sample_config_file(self):
        """Test creating sample configuration file."""
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            temp_filename = f.name

        try:
            create_sample_config(temp_filename)

            # Verify file was created and contains expected structure
            with open(temp_filename, 'r') as f:
                config = json.load(f)

            assert "database" in config
            assert "api" in config
            assert "logging" in config
            assert "features" in config
        finally:
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)

    # TODO: Add tests for file creation errors
    # TODO: Add tests for permission issues


# TODO: Add error path test class
class TestErrorPaths:
    """Test error handling and edge cases."""

    # TODO: Add comprehensive error tests here
    pass


# TODO: Add validation test class
class TestConfigValidation:
    """Test comprehensive configuration validation."""

    # TODO: Add validation tests here
    pass


# TODO: Add integration test class
class TestIntegration:
    """Test end-to-end configuration management scenarios."""

    # TODO: Add integration tests here
    pass
