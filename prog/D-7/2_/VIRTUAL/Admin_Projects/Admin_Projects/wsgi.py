"""
WSGI config for admin_CakeIFM_11 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Admin_Projects.settings")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin_MindMapFiles.settings")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin_CakeIFM_11.settings")

application = get_wsgi_application()
