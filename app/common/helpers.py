# Helper functions
import json
import os
import subprocess
from typing import Dict, Any

def ensure_directory_exists(directory_path: str):
    """Ensure a directory exists, create if it doesn't"""
    os.makedirs(directory_path, exist_ok=True)

def run_command(cmd: list, cwd: str = None) -> bool:
    """Run a shell command and return success status"""
    try:
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Command failed: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Error running command: {e}")
        return False

def validate_json_input(json_input: str) -> Dict[str, Any]:
    """Validate and parse JSON input"""
    try:
        return json.loads(json_input)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON input")