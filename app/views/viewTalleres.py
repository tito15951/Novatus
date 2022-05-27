from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()

def viewTalleres(request):
    try:
        correo=request.session['correo']
        rol=request.session['rol']
    except:
        correo='null'
        rol='null'
    talleres=Servi.listar_talleres()
    datos={'correo':correo,'rol':rol,'talleres':talleres}
    return render(request,'paginas/talleres.html',datos)