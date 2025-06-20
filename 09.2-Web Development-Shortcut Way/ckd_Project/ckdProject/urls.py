from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from ckdApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include app-level URLs with namespace
    path('ckdApp/', include(('ckdApp.urls', 'ckdApp'), namespace='ckdApp')),

    # Home page route
    path('', views.dataUploadView.as_view(), name='ckd'),

    # Add more view paths here if needed...
]

# Static/media files in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
