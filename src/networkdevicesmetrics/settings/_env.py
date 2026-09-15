from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

env = environ.Env(
    ALLOWED_HOSTS=(list, []),
    SECRET_KEY=(str, None),
)

environ.Env.read_env(BASE_DIR / ".env")
