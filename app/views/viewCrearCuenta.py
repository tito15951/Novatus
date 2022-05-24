from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()

def VistaCrearCuenta(request):
    marcas=["Kawasaki","Honda","Kymco","Susuki"]
    marcas.sort()
    print(marcas)
    datos={'marcas':marcas}
    return render(request,'paginas/crearCuenta.html',datos)

def CrearCuenta(request):
    print('Creando cuenta')
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
    print('Los datos son: ',nombre,' ',correo,' ',contrasena)
    if errores==0:
        resp=Servi.registrarse(correo,nombre,contrasena,moto)
        
        if(resp['Resp']):
            request.session['correo']=correo
            request.session['rol']=resp['Rol']
            return redirect('productosVer')
        else:
            print('Tiene errores en la información')
            return redirect('crearCuenta')    
    else:
        print('Tiene errores en la información')
        return redirect('crearCuenta')
    