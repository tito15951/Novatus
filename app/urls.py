from django.urls import path
from .views import viewIniciarSesion

urlpatterns = [
    path('login', viewIniciarSesion.vistaLogin,name='login'),
]
