from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()

def viewCitasTienda(request):
    correo=request.session['correo']
    citas=Servi.listar_citas_taller(correo)
    rol=request.session['rol']
    datos={'correo':correo,'rol':rol,'citas':citas}
    return render(request,'paginas/citas.html',datos)