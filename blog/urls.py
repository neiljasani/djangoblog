from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), # maps url to home function in views.py
    path('about/', views.about, name='blog-about')  # maps url to about function in views.py
]
