import socket

from .common import *

DEBUG = True

INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

INTERNAL_IPS = ["127.0.0.1"]