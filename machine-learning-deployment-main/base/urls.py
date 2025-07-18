from django import views
# birds/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bird_home'),  # Main page
    path('analyze/', views.analyze_audio, name='analyze_audio'),  # AJAX endpoint
]