from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()

def viewCrearAgendamiento(request):
    id=request.POST['id']
    taller=Servi.buscar_taller(id)
    servicios=["Cambio de aceite","Cambio de llanta"]
    marcas=["Susuki","Yamaha","Honda"]
    correo=request.session['correo']
    rol=request.session['rol']
    nombre_taller=f"{taller[0]['nombre']}-{taller[0]['direccion']}"
    datos={"servicios":servicios,"correo":correo,"rol":rol,"marcas":marcas,'taller':nombre_taller}
    return render(request,'paginas/crearAgendamiento.html',datos)