from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_release, name='upload_release'),
    path('releases/', views.release_list, name='release_list'),
]