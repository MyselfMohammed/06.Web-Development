"""
URL configuration for Concrete_Prediction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # combine path and include
from Concrete_Application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Concrete_Application/',include(('Concrete_Application.urls','Concrete_Application'),namespace='Concrete_Application')),
    #path('', views.FileUploadView.as_view(), name = 'image_upload'),
    #path('whats', views.WhatsappAnalaysis.as_view(), name = 'whats'),
    path('', views.dataUploadView.as_view(), name= 'upload_home'),
    #path('success', views.Success.as_view(), name = 'success'),
    #path('fail',views.Failure.as_view(),name='fail'),
    #path('filenot',views.FileNotfound.as_view(), name='filenot'),
    #path('aboutus',views.AboutUs.as_view(), name='aboutus')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
