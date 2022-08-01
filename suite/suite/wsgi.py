"""
WSGI config for suite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suite.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)