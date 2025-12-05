#!/usr/bin/env python3
"""
Script to validate and set up environment variables.
Run with: python setup_env.py
"""

import os
import sys
from pathlib import Path
import shutil


def setup_env():
    """Create .env from .env.example if it does not exist."""
    project_root = Path(__file__).parent
    env_file = project_root / ".env"
    env_example = project_root / ".env.example"

    if env_file.exists():
        print("✅ .env file already exists")
        return True

    if not env_example.exists():
        print("❌ .env.example file not found!")
        sys.exit(1)

    print("📋 .env file not found.")
    print(f"📋 Creating from .env.example...")
    shutil.copy(env_example, env_file)
    print(f"✅ Created: {env_file}")
    print("\n⚠️  IMPORTANT: Edit the .env file with your real values:")
    print(f"   {env_file}\n")

    return True


def validate_env():
    """Validate if the required variables are filled in."""
    from dotenv import load_dotenv

    project_root = Path(__file__).parent
    env_file = project_root / ".env"

    load_dotenv(dotenv_path=env_file)

    required_vars = ["CSV_URL", "GCS_BUCKET", "GCS_PATH"]
    missing = []
    empty = []

    for var in required_vars:
        value = os.getenv(var)
        if value is None:
            missing.append(var)
        elif value.strip() == "" or value.startswith("https://example"):
            empty.append(var)

    if missing:
        print(f"❌ Missing variables in .env: {', '.join(missing)}")
        sys.exit(1)

    if empty:
        print(f"⚠️  Empty variables or example values: {', '.join(empty)}")
        print("   Edit the .env file with your real values")
        sys.exit(1)

    print("✅ All variables are set!")
    for var in required_vars:
        print(f"   {var}: {os.getenv(var)[:50]}...")


if __name__ == "__main__":
    setup_env()
    validate_env()
