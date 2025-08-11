from django.urls import path
from . import views

urlpatterns = [
    path('center/', views.support_center, name='support_center'),
    path('create-ticket/', views.create_ticket, name='create_ticket'),
]