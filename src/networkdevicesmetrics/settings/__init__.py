import os

from django.core.exceptions import ImproperlyConfigured

_env = os.environ.get("DJANGO_ENV", "dev").lower()

if _env == "dev":
    from .dev import *  # noqa: F401,F403
elif _env == "prod":
    from .prod import *  # noqa: F401,F403
elif _env == "test":
    from .test import *  # noqa: F401,F403
else:
    raise ImproperlyConfigured(f"Unknown DJANGO_ENV: {_env!r}")
