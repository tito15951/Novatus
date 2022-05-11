from django.urls import path
from apiNovatus.views.producto import Product
from apiNovatus.views.usuario import User
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('usuarios', csrf_exempt(User.as_view()) ,name='usuarios'),
    path('productos',csrf_exempt(Product.as_view()) ,name='productos'),
]
