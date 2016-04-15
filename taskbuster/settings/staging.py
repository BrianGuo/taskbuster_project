# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
