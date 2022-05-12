from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()
def logear(request):
    if(request.POST):
        if(request.POST.get('email') and request.POST.get('contrasena')):
            correo=request.POST.get('email')
            contrasena=request.POST.get('contrasena')
            resp=Servi.iniciarSesion(correo,contrasena)
            print(resp)
            
    return render(request,'paginas/inisiarSesion.html')
def vistaLogin(request):
    return render(request,'paginas/inisiarSesion.html')