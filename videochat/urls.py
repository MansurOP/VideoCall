from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Correct import for settings
from django.conf.urls.static import static  # Import static for serving static files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('videochat_app.urls')),
]

# This is only needed in development mode to serve static files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
