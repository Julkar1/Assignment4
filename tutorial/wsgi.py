"""
WSGI config for tutorial project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#from tutorial.main import tutorial
 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')

application = get_wsgi_application()

if __name__ == "__main__":
        tutorial.run()