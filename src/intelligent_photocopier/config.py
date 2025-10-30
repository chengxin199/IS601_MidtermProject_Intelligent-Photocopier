"""
Configuration management for the Intelligent Photocopier.

This module handles API keys, settings, and environment configuration.
"""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


class Config:
    """Configuration manager for the Intelligent Photocopier."""

    def __init__(self):
        """Initialize configuration by loading environment variables."""
        # Load .env file if it exists
        env_path = Path.cwd() / ".env"
        if env_path.exists():
            load_dotenv(env_path)

        # Load configuration
        self.openai_api_key = self._get_openai_api_key()
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.max_tokens = int(os.getenv("MAX_TOKENS", "2000"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))

    def _get_openai_api_key(self) -> Optional[str]:
        """Get OpenAI API key from environment variables."""
        # Try multiple environment variable names
        key_names = ["OPENAI_API_KEY", "OPENAI_KEY", "API_KEY"]

        for key_name in key_names:
            api_key = os.getenv(key_name)
            if api_key:
                return api_key

        return None

    def is_configured(self) -> bool:
        """Check if all required configuration is available."""
        return self.openai_api_key is not None

    def get_missing_config(self) -> list:
        """Get list of missing configuration items."""
        missing = []

        if not self.openai_api_key:
            missing.append("OpenAI API Key (set OPENAI_API_KEY environment variable)")

        return missing

    def create_sample_env_file(self) -> str:
        """Create a sample .env file with configuration template."""
        sample_content = """# Intelligent Photocopier Configuration
# Copy this file to .env and fill in your API key

# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Model Configuration (defaults shown)
OPENAI_MODEL=gpt-4o-mini
MAX_TOKENS=2000
TEMPERATURE=0.7

# Usage:
# 1. Get your API key from https://platform.openai.com/api-keys
# 2. Replace 'your_openai_api_key_here' with your actual API key
# 3. Save this file as '.env' in the project root directory
"""

        env_file_path = Path.cwd() / ".env.example"
        with open(env_file_path, "w") as f:
            f.write(sample_content)

        return str(env_file_path)


# Global configuration instance
config = Config()
