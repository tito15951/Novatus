from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios

Servi=Servicios()

def vistaAgendamiento(request):
    correo=request.session['correo']
    rol=request.session['rol']
    datos={'correo':correo,'rol':rol}
    #print(datos)
    return render(request,'paginas/agendamiento.html',datos)