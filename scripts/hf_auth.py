from __future__ import annotations

import getpass
import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV_PATH = ROOT / ".env"


def load_hf_token(env_var: str = "HF_TOKEN", env_file: str | Path | None = None) -> str:
    """Load a Hugging Face read token from the environment or a local .env file."""
    target = Path(env_file) if env_file is not None else DEFAULT_ENV_PATH
    load_dotenv(target, override=False)

    token = os.environ.get(env_var, "").strip()
    if token:
        return token

    token = getpass.getpass("Paste your Hugging Face READ token (hf_...): ").strip()
    if not token:
        raise ValueError(
            "HF_TOKEN is missing. Create a local .env file from .env.example or set the "
            "HF_TOKEN environment variable before loading the warehouse."
        )
    return token


if __name__ == "__main__":
    token = load_hf_token()
    print(f"HF_TOKEN loaded: {token[:6]}...{token[-4:]}")
