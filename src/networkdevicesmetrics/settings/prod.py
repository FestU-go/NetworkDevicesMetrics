from django.core.exceptions import ImproperlyConfigured

from ._env import env
from .base import *  # noqa: F401,F403

DEBUG = False

if not ALLOWED_HOSTS:
    raise ImproperlyConfigured("ALLOWED_HOSTS must be set in production")

DATABASES = {"default": env.db("DATABASE_URL")}
