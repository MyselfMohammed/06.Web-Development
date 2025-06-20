
from Concrete_Application import views
from django.urls import path, re_path

app_name = 'Concrete_Application'

urlpatterns = [
    path('', views.dataUploadView.as_view(), name = 'upload_home'), # -> Calling a Function - dataUploadView from the File - view.py
]
