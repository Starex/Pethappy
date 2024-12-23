from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('agregar-mascota/', views.agregar_mascota, name='agregar_mascota'),
]