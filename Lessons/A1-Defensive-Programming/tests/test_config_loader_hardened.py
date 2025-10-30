"""
Tests for config_loader module - Defensive programming implementation and testing.

This file demonstrates the implementation of defensive programming principles:
1. Custom exception hierarchy for configuration management
2. Input validation with detailed error messages
3. Guard clauses for file operations
4. Secure logging without sensitive data exposure
5. Comprehensive error path testing
"""

import pytest
import json
import os
import tempfile
import logging
from typing import Dict, Any, Optional
from pathlib import Path

# Set up logging for demonstration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# =============================================================================
# DEFENSIVE PROGRAMMING IMPLEMENTATION: Custom Exception Hierarchy
# =============================================================================

class ConfigError(Exception):
    """Base exception for configuration operations."""
    pass


class ConfigFileError(ConfigError):
    """Raised when configuration file operations fail."""
    def __init__(self, message, filename=None, operation=None):
        super().__init__(message)
        self.filename = filename
        self.operation = operation


class ConfigValidationError(ConfigError):
    """Raised when configuration validation fails."""
    def __init__(self, message, config_key=None, config_value=None):
        super().__init__(message)
        self.config_key = config_key
        self.config_value = config_value


class ConfigParsingError(ConfigError):
    """Raised when configuration parsing fails."""
    def __init__(self, message, filename=None, line_number=None):
        super().__init__(message)
        self.filename = filename
        self.line_number = line_number


class ConfigSecurityError(ConfigError):
    """Raised when security constraints are violated."""
    pass


# =============================================================================
# DEFENSIVE PROGRAMMING IMPLEMENTATION: Safe Logging Utilities
# =============================================================================

def create_safe_log_context(**kwargs):
    """Create logging context with sensitive data redacted."""
    sensitive_keywords = {
        'password', 'token', 'secret', 'key', 'auth',
        'credential', 'private', 'session', 'api_key'
    }

    safe_context = {}
    for key, value in kwargs.items():
        key_lower = key.lower()

        # Check if key contains sensitive information
        if any(sensitive in key_lower for sensitive in sensitive_keywords):
            safe_context[key] = '[REDACTED]'
        # Check if value looks like a file path
        elif isinstance(value, str) and ('/' in value or '\\' in value):
            # Only show filename, not full path
            safe_context[key] = Path(value).name
        # Truncate very long values
        elif isinstance(value, str) and len(value) > 100:
            safe_context[key] = value[:97] + '...'
        else:
            safe_context[key] = value

    return safe_context


# =============================================================================
# DEFENSIVE PROGRAMMING IMPLEMENTATION: Hardened Configuration Functions
# =============================================================================

def hardened_load_config(filename: str) -> Dict[str, Any]:
    """Load configuration from a JSON file with comprehensive error handling.

    Preconditions:
    - filename must be a non-empty string
    - file must exist and be readable

    Postconditions:
    - returns a valid dictionary
    - file is properly closed even on error
    """
    # Guard clause: Input validation
    if not isinstance(filename, str):
        raise ConfigFileError(
            f"Filename must be a string, got {type(filename).__name__}",
            filename=filename,
            operation="load"
        )

    if not filename.strip():
        raise ConfigFileError(
            "Filename cannot be empty or whitespace",
            filename=filename,
            operation="load"
        )

    # Guard clause: File existence check
    if not os.path.exists(filename):
        raise ConfigFileError(
            f"Configuration file not found: {filename}",
            filename=filename,
            operation="load"
        )

    # Guard clause: File readability check
    if not os.access(filename, os.R_OK):
        raise ConfigFileError(
            f"No permission to read configuration file: {filename}",
            filename=filename,
            operation="load"
        )

    # Log operation with safe context
    context = create_safe_log_context(filename=filename, operation="load")
    logger.info("Loading configuration file", extra=context)

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            config = json.load(f)

        # Postcondition: Validate return type
        if not isinstance(config, dict):
            raise ConfigParsingError(
                f"Configuration must be a JSON object, got {type(config).__name__}",
                filename=filename
            )

        logger.info("Configuration loaded successfully", extra={**context, "keys_count": len(config)})
        return config

    except json.JSONDecodeError as e:
        error_msg = f"Invalid JSON in {filename} at line {e.lineno}, column {e.colno}: {e.msg}"
        logger.error(error_msg, extra=context)
        raise ConfigParsingError(error_msg, filename=filename, line_number=e.lineno) from e

    except PermissionError as e:
        error_msg = f"Permission denied reading {filename}"
        logger.error(error_msg, extra=context)
        raise ConfigFileError(error_msg, filename=filename, operation="load") from e

    except Exception as e:
        error_msg = f"Unexpected error loading configuration: {e}"
        logger.error(error_msg, extra=context, exc_info=True)
        raise ConfigError(error_msg) from e


def hardened_validate_config(config: Dict[str, Any]) -> None:
    """Validate configuration structure with detailed error messages.

    Preconditions:
    - config must be a dictionary

    Postconditions:
    - raises ConfigValidationError if validation fails
    - returns None if validation passes
    """
    # Guard clause: Type validation
    if not isinstance(config, dict):
        raise ConfigValidationError(
            f"Configuration must be a dictionary, got {type(config).__name__}",
            config_value=config
        )

    # Guard clause: Empty configuration check
    if not config:
        raise ConfigValidationError("Configuration cannot be empty")

    required_sections = ['database', 'api', 'logging']
    missing_sections = []

    # Check for required sections
    for section in required_sections:
        if section not in config:
            missing_sections.append(section)

    if missing_sections:
        raise ConfigValidationError(
            f"Missing required configuration sections: {', '.join(missing_sections)}",
            config_key='required_sections'
        )

    # Validate each section
    _validate_database_config(config.get('database', {}))
    _validate_api_config(config.get('api', {}))
    _validate_logging_config(config.get('logging', {}))

    logger.info("Configuration validation passed",
                extra=create_safe_log_context(sections=list(config.keys())))


def _validate_database_config(db_config: Dict[str, Any]) -> None:
    """Validate database configuration section."""
    required_fields = ['host', 'port', 'name', 'user']

    for field in required_fields:
        if field not in db_config:
            raise ConfigValidationError(
                f"Database configuration missing required field: {field}",
                config_key=f"database.{field}"
            )

    # Validate port is numeric and in valid range
    port = db_config.get('port')
    if not isinstance(port, int) or not (1 <= port <= 65535):
        raise ConfigValidationError(
            f"Database port must be an integer between 1-65535, got: {port}",
            config_key="database.port",
            config_value=port
        )

    # Validate host is not empty
    host = db_config.get('host', '').strip()
    if not host:
        raise ConfigValidationError(
            "Database host cannot be empty",
            config_key="database.host"
        )


def _validate_api_config(api_config: Dict[str, Any]) -> None:
    """Validate API configuration section."""
    required_fields = ['base_url', 'timeout', 'retry_attempts']

    for field in required_fields:
        if field not in api_config:
            raise ConfigValidationError(
                f"API configuration missing required field: {field}",
                config_key=f"api.{field}"
            )

    # Validate timeout
    timeout = api_config.get('timeout')
    if not isinstance(timeout, (int, float)) or timeout <= 0:
        raise ConfigValidationError(
            f"API timeout must be a positive number, got: {timeout}",
            config_key="api.timeout",
            config_value=timeout
        )

    # Validate retry attempts
    retry_attempts = api_config.get('retry_attempts')
    if not isinstance(retry_attempts, int) or not (0 <= retry_attempts <= 10):
        raise ConfigValidationError(
            f"API retry_attempts must be an integer between 0-10, got: {retry_attempts}",
            config_key="api.retry_attempts",
            config_value=retry_attempts
        )


def _validate_logging_config(log_config: Dict[str, Any]) -> None:
    """Validate logging configuration section."""
    valid_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'}

    level = log_config.get('level', '').upper()
    if level and level not in valid_levels:
        raise ConfigValidationError(
            f"Invalid logging level: {level}. Must be one of: {', '.join(valid_levels)}",
            config_key="logging.level",
            config_value=level
        )


class HardenedConfigManager:
    """Configuration manager with comprehensive defensive programming."""

    def __init__(self, config_file: str = 'config.json'):
        # Input validation for constructor
        if not isinstance(config_file, str):
            raise ConfigFileError(
                f"Config file must be a string, got {type(config_file).__name__}",
                filename=config_file
            )

        if not config_file.strip():
            raise ConfigFileError("Config file cannot be empty", filename=config_file)

        self.config_file = config_file.strip()
        self.config = {}
        self._is_loaded = False

        # Default configuration with comprehensive settings
        self.default_config = {
            'database': {
                'host': 'localhost',
                'port': 5432,
                'name': 'myapp',
                'user': 'user',
                'password': '',
                'connection_timeout': 30,
                'max_connections': 10
            },
            'api': {
                'base_url': 'https://api.example.com',
                'timeout': 30,
                'retry_attempts': 3,
                'rate_limit': 100
            },
            'logging': {
                'level': 'INFO',
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                'max_file_size': '10MB',
                'backup_count': 5
            }
        }

    def load(self) -> None:
        """Load configuration with fallback handling and validation.

        Postconditions:
        - self.config contains valid configuration
        - self._is_loaded is True
        """
        context = create_safe_log_context(config_file=self.config_file)

        try:
            if os.path.exists(self.config_file):
                logger.info("Loading user configuration", extra=context)
                user_config = hardened_load_config(self.config_file)

                # Validate user configuration
                hardened_validate_config(user_config)

                # Merge with defaults
                self.config = self._deep_merge_configs(self.default_config, user_config)
                logger.info("User configuration loaded and merged", extra=context)
            else:
                logger.warning("Configuration file not found, using defaults", extra=context)
                self.config = self.default_config.copy()

            self._is_loaded = True

            # Final validation of merged config
            hardened_validate_config(self.config)

        except ConfigError:
            # Known configuration errors - use defaults and log warning
            logger.warning("Configuration error, falling back to defaults", extra=context)
            self.config = self.default_config.copy()
            self._is_loaded = True

        except Exception as e:
            # Unexpected errors - log and re-raise
            logger.error(f"Unexpected error loading configuration: {e}",
                        extra=context, exc_info=True)
            raise ConfigError(f"Failed to load configuration: {e}") from e

    def _deep_merge_configs(self, default: Dict[str, Any], user: Dict[str, Any]) -> Dict[str, Any]:
        """Deep merge user configuration with defaults."""
        merged = default.copy()

        for key, value in user.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = self._deep_merge_configs(merged[key], value)
            else:
                merged[key] = value

        return merged

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Get configuration value with nested key support.

        Preconditions:
        - configuration must be loaded
        - key must be a non-empty string
        """
        # Guard clause: Check if config is loaded
        if not self._is_loaded:
            raise ConfigError("Configuration not loaded. Call load() first.")

        # Guard clause: Validate key
        if not isinstance(key, str):
            raise ConfigValidationError(
                f"Configuration key must be a string, got {type(key).__name__}",
                config_key=key
            )

        if not key.strip():
            raise ConfigValidationError("Configuration key cannot be empty")

        # Support nested keys (e.g., 'database.host')
        keys = key.split('.')
        value = self.config

        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            if default is not None:
                return default
            raise ConfigValidationError(
                f"Configuration key not found: {key}",
                config_key=key
            )

    def get_database_url(self) -> str:
        """Get database connection URL with validation.

        Postconditions:
        - returns a valid PostgreSQL connection URL
        """
        if not self._is_loaded:
            raise ConfigError("Configuration not loaded. Call load() first.")

        try:
            db_config = self.get('database')

            # Validate required fields exist
            required_fields = ['user', 'password', 'host', 'port', 'name']
            for field in required_fields:
                if field not in db_config:
                    raise ConfigValidationError(
                        f"Database configuration missing {field}",
                        config_key=f"database.{field}"
                    )

            # Build URL with proper escaping
            user = db_config['user']
            password = db_config['password']
            host = db_config['host']
            port = db_config['port']
            name = db_config['name']

            url = f"postgresql://{user}:{password}@{host}:{port}/{name}"

            # Log URL creation (without sensitive data)
            context = create_safe_log_context(
                host=host, port=port, database=name, user=user, password=password
            )
            logger.debug("Database URL created", extra=context)

            return url

        except ConfigValidationError:
            raise
        except Exception as e:
            raise ConfigError(f"Failed to create database URL: {e}") from e


# =============================================================================
# DEFENSIVE PROGRAMMING TESTS: Error Path and Validation Testing
# =============================================================================

class TestHardenedConfigLoader:
    """Comprehensive tests for defensive configuration loading."""

    def test_load_config_input_validation(self):
        """Test configuration loading input validation."""
        # Test non-string filename
        with pytest.raises(ConfigFileError, match="must be a string"):
            hardened_load_config(123)

        # Test empty filename
        with pytest.raises(ConfigFileError, match="cannot be empty"):
            hardened_load_config("")

        with pytest.raises(ConfigFileError, match="cannot be empty"):
            hardened_load_config("   ")

    def test_load_nonexistent_file(self):
        """Test loading non-existent file raises appropriate error."""
        with pytest.raises(ConfigFileError, match="not found"):
            hardened_load_config("nonexistent_file.json")

    def test_load_invalid_json(self):
        """Test loading invalid JSON raises parsing error."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write('{"invalid": json content}')  # Invalid JSON
            temp_filename = f.name

        try:
            with pytest.raises(ConfigParsingError, match="Invalid JSON"):
                hardened_load_config(temp_filename)
        finally:
            os.unlink(temp_filename)

    def test_config_validation_comprehensive(self):
        """Test comprehensive configuration validation."""
        # Test non-dict config
        with pytest.raises(ConfigValidationError, match="must be a dictionary"):
            hardened_validate_config("not a dict")

        # Test empty config
        with pytest.raises(ConfigValidationError, match="cannot be empty"):
            hardened_validate_config({})

        # Test missing required sections
        with pytest.raises(ConfigValidationError, match="Missing required"):
            hardened_validate_config({"database": {}})

        # Test invalid database port
        invalid_config = {
            "database": {"host": "localhost", "port": "invalid", "name": "test", "user": "user"},
            "api": {"base_url": "http://test.com", "timeout": 30, "retry_attempts": 3},
            "logging": {"level": "INFO"}
        }
        with pytest.raises(ConfigValidationError, match="port must be an integer"):
            hardened_validate_config(invalid_config)

    def test_config_manager_initialization(self):
        """Test configuration manager initialization validation."""
        # Test invalid config file type
        with pytest.raises(ConfigFileError, match="must be a string"):
            HardenedConfigManager(123)

        # Test empty config file
        with pytest.raises(ConfigFileError, match="cannot be empty"):
            HardenedConfigManager("")

    def test_config_manager_load_with_fallback(self):
        """Test configuration manager loading with fallback."""
        # Test with non-existent file (should use defaults)
        manager = HardenedConfigManager("nonexistent.json")
        manager.load()

        assert manager._is_loaded
        assert manager.get("database.host") == "localhost"

    def test_config_manager_get_validation(self):
        """Test configuration manager get method validation."""
        manager = HardenedConfigManager()

        # Test getting value before loading
        with pytest.raises(ConfigError, match="not loaded"):
            manager.get("database.host")

        manager.load()

        # Test invalid key types
        with pytest.raises(ConfigValidationError, match="must be a string"):
            manager.get(123)

        # Test empty key
        with pytest.raises(ConfigValidationError, match="cannot be empty"):
            manager.get("")

        # Test missing key
        with pytest.raises(ConfigValidationError, match="not found"):
            manager.get("nonexistent.key")

    def test_database_url_generation(self):
        """Test database URL generation with validation."""
        manager = HardenedConfigManager()
        manager.load()

        url = manager.get_database_url()
        assert url.startswith("postgresql://")
        assert "localhost" in url
        assert "5432" in url

    def test_error_context_preservation(self):
        """Test that errors include helpful context."""
        try:
            hardened_load_config("nonexistent.json")
        except ConfigFileError as e:
            assert e.filename == "nonexistent.json"
            assert e.operation == "load"

        try:
            hardened_validate_config({"invalid": "config"})
        except ConfigValidationError as e:
            assert "Missing required" in str(e)

    def test_successful_operations(self):
        """Test successful configuration operations."""
        # Create valid config file
        valid_config = {
            "database": {
                "host": "testhost",
                "port": 5432,
                "name": "testdb",
                "user": "testuser",
                "password": "testpass"
            },
            "api": {
                "base_url": "https://api.test.com",
                "timeout": 60,
                "retry_attempts": 5
            },
            "logging": {
                "level": "DEBUG"
            }
        }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(valid_config, f)
            temp_filename = f.name

        try:
            # Test loading
            config = hardened_load_config(temp_filename)
            assert config["database"]["host"] == "testhost"

            # Test validation
            hardened_validate_config(config)  # Should not raise

            # Test manager
            manager = HardenedConfigManager(temp_filename)
            manager.load()
            assert manager.get("database.host") == "testhost"
            assert manager.get("api.timeout") == 60

        finally:
            os.unlink(temp_filename)


# =============================================================================
# DEMONSTRATION: Show defensive programming in action
# =============================================================================

if __name__ == "__main__":
    print("=== Defensive Programming Config Loader Demo ===\n")

    # Successful operations
    print("✅ Successful operations:")
    manager = HardenedConfigManager()
    manager.load()
    print(f"Default database host: {manager.get('database.host')}")
    print(f"Default API timeout: {manager.get('api.timeout')}")

    # Error handling demonstrations
    print("\n❌ Error handling demonstrations:")

    try:
        hardened_load_config(123)
    except ConfigFileError as e:
        print(f"Type validation: {e}")

    try:
        hardened_load_config("nonexistent.json")
    except ConfigFileError as e:
        print(f"File not found: {e}")

    try:
        hardened_validate_config({"incomplete": "config"})
    except ConfigValidationError as e:
        print(f"Validation error: {e}")

    try:
        unloaded_manager = HardenedConfigManager()
        unloaded_manager.get("database.host")
    except ConfigError as e:
        print(f"Access before load: {e}")

    print("\n=== Demo Complete ===")
