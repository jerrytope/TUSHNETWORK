from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.analytics_dashboard, name='analytics_dashboard'),
    path('royalties/', views.royalties, name='royalties'),
    path('withdraw/', views.request_withdrawal, name='request_withdrawal'),
]