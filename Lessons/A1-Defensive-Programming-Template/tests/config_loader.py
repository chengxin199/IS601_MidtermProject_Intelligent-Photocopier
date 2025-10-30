"""
Configuration loader module for defensive programming practice.

This module loads and parses configuration files but lacks robust
error handling and validation.

Your task: Harden this module by applying defensive programming principles.
"""

import json
import os
from typing import Any, Dict, Optional


def load_config(filename: str) -> Dict[str, Any]:
    """Load configuration from a JSON file."""
    # TODO: Add proper error handling
    with open(filename, "r") as f:
        config = json.load(f)
    return config


def validate_config(config: Dict[str, Any]) -> bool:
    """Validate configuration structure and values."""
    # TODO: Add comprehensive validation
    required_keys = ["database", "api", "logging"]

    for key in required_keys:
        if key not in config:
            return False

    return True


def get_database_config(config: Dict[str, Any]) -> Dict[str, str]:
    """Extract database configuration."""
    # TODO: Add validation and error handling
    db_config = config["database"]
    return {
        "host": db_config["host"],
        "port": db_config["port"],
        "name": db_config["name"],
        "user": db_config["user"],
        "password": db_config["password"],
    }


def get_api_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Extract API configuration."""
    # TODO: Add validation and error handling
    api_config = config["api"]
    return {
        "base_url": api_config["base_url"],
        "timeout": api_config["timeout"],
        "retry_attempts": api_config["retry_attempts"],
        "api_key": api_config.get("api_key", ""),
    }


def merge_configs(default_config: Dict[str, Any], user_config: Dict[str, Any]) -> Dict[str, Any]:
    """Merge user configuration with defaults."""
    # TODO: Add proper deep merging and validation
    merged = default_config.copy()
    merged.update(user_config)
    return merged


class ConfigManager:
    """Manages application configuration."""

    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.config = {}
        self.default_config = {
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "myapp",
                "user": "user",
                "password": "",
            },
            "api": {"base_url": "https://api.example.com", "timeout": 30, "retry_attempts": 3},
            "logging": {
                "level": "INFO",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        }

    def load(self) -> None:
        """Load configuration from file."""
        # TODO: Add proper error handling and fallbacks
        if os.path.exists(self.config_file):
            user_config = load_config(self.config_file)
            if validate_config(user_config):
                self.config = merge_configs(self.default_config, user_config)
            else:
                # Fallback to defaults
                self.config = self.default_config
        else:
            # Use defaults if file doesn't exist
            self.config = self.default_config

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Get configuration value by key."""
        # TODO: Add support for nested keys (e.g., 'database.host')
        return self.config.get(key, default)

    def get_database_url(self) -> str:
        """Get database connection URL."""
        # TODO: Add validation and error handling
        db_config = self.config["database"]
        return f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}"

    def save(self, filename: Optional[str] = None) -> None:
        """Save current configuration to file."""
        # TODO: Add error handling
        target_file = filename or self.config_file
        with open(target_file, "w") as f:
            json.dump(self.config, f, indent=2)

    def reload(self) -> None:
        """Reload configuration from file."""
        # TODO: Add error handling and backup of current config
        self.load()


def create_sample_config(filename: str = "sample_config.json") -> None:
    """Create a sample configuration file."""
    # TODO: Add error handling
    sample_config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp_prod",
            "user": "admin",
            "password": "secret123",
        },
        "api": {
            "base_url": "https://api.production.com",
            "timeout": 60,
            "retry_attempts": 5,
            "api_key": "your-api-key-here",
        },
        "logging": {
            "level": "WARNING",
            "format": "%(asctime)s - %(levelname)s - %(message)s",
            "file": "/var/log/myapp.log",
        },
        "features": {"enable_caching": True, "cache_ttl": 3600, "enable_monitoring": True},
    }

    with open(filename, "w") as f:
        json.dump(sample_config, f, indent=2)


if __name__ == "__main__":
    # Simple test cases
    print("Testing configuration loader...")

    # Create sample config for testing
    create_sample_config()

    # Test configuration manager
    config_manager = ConfigManager("sample_config.json")
    config_manager.load()

    print(f"Database URL: {config_manager.get_database_url()}")
    print(f"API timeout: {config_manager.get('api', {}).get('timeout', 'N/A')}")
    print(f"Logging level: {config_manager.get('logging', {}).get('level', 'N/A')}")

    # Test with non-existent file
    config_manager2 = ConfigManager("nonexistent.json")
    config_manager2.load()
    print(f"\\nFallback config loaded successfully")
