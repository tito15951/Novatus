from django.urls import path
from .views import viewIniciarSesion
from .views import viewCrearCuenta
from .views import viewNuestrosProductos

urlpatterns = [
    path('login', viewIniciarSesion.vistaLogin,name='login'),
    path('crearCuenta',viewCrearCuenta.VistaCrearCuenta,name='crearCuenta'),
    path('productos',viewNuestrosProductos.vistaProductos,name='productos'),



    #peticiones
    path('logearse',viewIniciarSesion.logear,name='logearse')
]
