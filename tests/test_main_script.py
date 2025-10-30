"""
Test for the __main__ execution block of main.py
"""

import subprocess
import sys
from pathlib import Path


def test_main_module_execution():
    """Test running the main module directly to cover __name__ == '__main__' block."""
    # Run as a module with --help flag to test the main() entry point
    result = subprocess.run(
        [sys.executable, "-m", "src.intelligent_photocopier.main", "--help"],
        capture_output=True,
        text=True,
        timeout=5,
        cwd=str(Path(__file__).parent.parent),
    )

    # Should execute successfully and print help
    assert result.returncode == 0
    assert "Intelligent Photocopier" in result.stdout or "Usage" in result.stdout
