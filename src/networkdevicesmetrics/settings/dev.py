from ._env import BASE_DIR, env
from .base import *  # noqa: F401,F403

DEBUG = True

if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = [
        "127.0.0.1",
        "localhost",
    ]


if env("DATABASE_URL", default=None):
    DATABASES = {"default": env.db("DATABASE_URL")}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
