from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()

def VistaCrearCuenta(request):
    try:
        correo=request.session['correo']
        rol=request.session['rol']
    except:
        correo='null'
        rol='null'
    datos={'correo':correo,'rol':rol}
    return render(request,'paginas/crearCuenta.html',datos)

def CrearCuenta(request):
    nombre=request.POST.get('nombre')
    correo=request.POST.get('email')
    contrasena=request.POST.get('contrasena')
    errores=0
    if len(nombre)<4:
        errores+=1
        messages.error(request,'Por favor, ingrese su nombre')
    if len(correo)<5:
        errores+=1
        messages.error(request,'Por favor, ingrese un correo valido')
    if len(contrasena)<8:
        errores+=1
        messages.error(request,'Ingrese una contraseña mas larga')
    if errores==0:
        resp=Servi.registrarse(correo,nombre,contrasena)
        
        if(resp['Resp']):
            request.session['correo']=correo
            request.session['rol']='cliente'
            # return redirect('productosVer')
            return redirect('talleresAliados')
            
        else:
            messages.error(request,'El correo ya se encuentra registrado')
            return redirect('crearCuenta')    
    else:
        return redirect('crearCuenta')
    