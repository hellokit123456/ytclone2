from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel (YouTube-like content manager)
    path('admin/', admin.site.urls),

    # API Routes
    path('api/', include('api.urls')),  # All API logic in api/urls.py
]

# Serve media files (videos, thumbnails) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
