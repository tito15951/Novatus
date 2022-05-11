from django.urls import path
from .views import viewIniciarSesion
from .views import viewCrearCuenta

urlpatterns = [
    path('login', viewIniciarSesion.vistaLogin,name='login'),
    path('crearCuenta',viewCrearCuenta.VistaCrearCuenta,name='crearCuenta'),
]
