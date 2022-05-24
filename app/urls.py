from django.urls import path
from .views import viewIniciarSesion
from .views import viewCrearCuenta
from .views import viewNuestrosProductos
from .views import viewAgendamiento
from .views import viewCrearAgendamiento
from .views import viewIndex
urlpatterns = [
    path('',viewIndex.viewIndex,name='index'),
    path('login', viewIniciarSesion.vistaLogin,name='login'),
    path('crearCuenta',viewCrearCuenta.VistaCrearCuenta,name='crearCuenta'),
    path('productos',viewNuestrosProductos.vistaProductos,name='productosVer'),
    path('agendamiento',viewAgendamiento.vistaAgendamiento,name='agendamiento'),
    path('crearAgendamiento',viewCrearAgendamiento.viewCrearAgendamiento,name='crearAgendamiento'),

    #peticiones
    path('cerrarSesion',viewIniciarSesion.cerrarSesion,name='cerrarSesion'),
    path('logearse',viewIniciarSesion.logear,name='logearse'),
    path('crearCuentaPeticion',viewCrearCuenta.CrearCuenta,name='crearCuentaPeticion'),
]
