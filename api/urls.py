from django.urls import path, include
from . import views as views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('api/', include('api.api_urls')),
    path('', views.home_view, name='home'),
    path('file/<int:id>/view', views.file_view, name='file-detail'),
    path('file/<int:id>/share', views.share_view, name='file-share'),
]