from django.urls import path
from apiNovatus.views.usuario import User
from apiNovatus.views.talleres import workshops
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('usuarios', csrf_exempt(User.as_view()) ,name='usuarios'),
    path('talleres', csrf_exempt(workshops.as_view()) ,name='talleres'),
]
