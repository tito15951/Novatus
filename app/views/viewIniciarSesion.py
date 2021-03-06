from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()
def cerrarSesion(request):
    try:
        del request.session['correo']
        del request.session['rol']
        return redirect('index')
    except:
        return redirect('index')

def logear(request):
    if(request.POST):
        if(request.POST.get('email') and request.POST.get('contrasena')):
            correo=request.POST.get('email')
            contrasena=request.POST.get('contrasena')
            resp=Servi.iniciarSesion(correo,contrasena)
            if resp['Resp']:
                request.session['correo']=correo
                request.session['rol']=resp['rol']
                if resp['rol']=='cliente':
                    return redirect('agendamiento')
                elif resp['rol']=='tienda':
                    return redirect('citasTienda')
                else:
                    return redirect('gestionarTalleres')
            else:
                messages.error(request,'Usuario o contraseña incorrecta')
                return HttpResponseRedirect('login')
        else:
            messages.error(request,'Ingrese todos los campos')
            return HttpResponseRedirect('login')
def vistaLogin(request):
    try:
        correo=request.session['correo']
        rol=request.session['rol']
    except:
        correo='null'
        rol='null'
    datos={'correo':correo,'rol':rol}
    return render(request,'paginas/inisiarSesion.html',datos)