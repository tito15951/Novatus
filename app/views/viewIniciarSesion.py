from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()
def cerrarSesion(request):
    try:
        del request.session['correo']
        del request.session['rol']
    except:
        return redirect('login')

def logear(request):
    if(request.POST):
        if(request.POST.get('email') and request.POST.get('contrasena')):
            correo=request.POST.get('email')
            contrasena=request.POST.get('contrasena')
            resp=Servi.iniciarSesion(correo,contrasena)
            request.session['correo']=correo
            request.session['rol']=resp['Resp']
            print('Guardando en caché correctamente')
            return redirect('agendamiento')
        else:
            messages.error('Ingrese todos los campos')
            print('Faltan datos')
            return HttpResponseRedirect('login')
def vistaLogin(request):
    try:
        correo=request.session['correo']
        rol=request.session['rol']
    except:
        correo='null'
        rol='null'
    datos={'correo':correo,'rol':rol}
    print(datos)
    return render(request,'paginas/inisiarSesion.html',datos)