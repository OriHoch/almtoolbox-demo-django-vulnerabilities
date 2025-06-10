from django.urls import path

from . import views

urlpatterns = [
    path('vulnerable/', views.vulnerable, name='vulnerable'),
]
