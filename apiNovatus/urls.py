from django.urls import path
from apiNovatus.views.citas import mostrar_citas
from apiNovatus.views.comentarios import mostrar_comentarios
from apiNovatus.views.usuario import User
from apiNovatus.views.talleres import workshops
from apiNovatus.views.chat import Conversacion
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('usuarios', csrf_exempt(User.as_view()) ,name='usuarios'),
    path('talleres', csrf_exempt(workshops.as_view()) ,name='talleres'),
    path('comentarios', csrf_exempt(mostrar_comentarios.as_view()) ,name='cometarios'),
    path('citas', csrf_exempt(mostrar_citas.as_view()) ,name='citas'),
    path('chat',csrf_exempt(Conversacion.as_view()),name='chat'),
]
