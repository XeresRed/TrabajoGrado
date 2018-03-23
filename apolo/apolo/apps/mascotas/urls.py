
from django.urls import path
from apps.mascotas import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nuevo', views.mascota_view, name="crear"),
]
