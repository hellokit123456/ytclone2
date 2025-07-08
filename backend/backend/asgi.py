import os
from django.core.asgi import get_asgi_application

# Set the default settings module for 'backend' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Get the ASGI application callable
application = get_asgi_application()
