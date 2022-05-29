from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()

def viewCitasTienda(request):
    correo=request.session['correo']
    citas=Servi.listar_citas_taller(correo)
    #print(citas)
    for cita in citas:
        cita['fecha']=cita['fecha_hora'].split(' ')[0]
        cita['hora']=cita['fecha_hora'].split(' ')[1][0:5]

        print(cita)
    rol=request.session['rol']
    datos={'correo':correo,'rol':rol,'citas':citas}
    return render(request,'paginas/citas.html',datos)