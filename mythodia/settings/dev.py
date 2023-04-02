# flake8: noqa

from .base import *

import platform

current_os = platform.system()


INSTALLED_APPS += [
    "debug_toolbar",
    "django_browser_reload",
]
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]


CORS_ALLOW_ALL_ORIGINS = True

# ==============================================================================
# CORE SETTINGS
# ==============================================================================
if current_os == "Windows":
    NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
