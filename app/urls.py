from django.urls import path
from .views import viewIniciarSesion
from .views import viewCrearCuenta
from .views import viewAgendamiento
from .views import viewCrearAgendamiento
from .views import viewModificarAgendamiento
from .views import viewIndex
from .views import viewCitasTienda
from .views import viewTalleres
from .views import viewChat
from .views import viewMisAgendamientos
urlpatterns = [
    path('',viewIndex.viewIndex,name='index'),
    path('login', viewIniciarSesion.vistaLogin,name='login'),
    path('crearCuenta',viewCrearCuenta.VistaCrearCuenta,name='crearCuenta'),
    path('agendamiento',viewAgendamiento.vistaAgendamiento,name='agendamiento'),
    path('crearAgendamiento',viewCrearAgendamiento.viewCrearAgendamiento,name='crearAgendamiento'),
    path('modificarAgendamiento',viewModificarAgendamiento.viewModificarAgendamiento,name='modificarAgendamiento'),
    path('citasTienda',viewCitasTienda.viewCitasTienda,name='citasTienda'),
    path('talleresAliados',viewTalleres.viewTalleres,name='talleresAliados'),
    path('chat',viewChat.vistaChat,name='chat'),
    path('misAgendamientos',viewMisAgendamientos.viewMisAgendamientos,name='misAgendamientos'),
    #peticiones
    path('cerrarSesion',viewIniciarSesion.cerrarSesion,name='cerrarSesion'),
    path('logearse',viewIniciarSesion.logear,name='logearse'),
    path('crearCuentaPeticion',viewCrearCuenta.CrearCuenta,name='crearCuentaPeticion'),
    path('nuevoMensaje',viewChat.nuevoMensaje,name='nuevoMensaje'),
]
