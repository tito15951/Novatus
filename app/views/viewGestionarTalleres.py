from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect

from app.formTaller import FotoForm
from app.models import Foto
from ..services import Servicios
Servi=Servicios()


def viewGestion(request):
    correo=request.session['correo']
    rol=request.session['rol']
    talleres=Servi.listar_talleres()
    usuarios_disponibles=Servi.listar_candidatis_administrador()
    datos={'correo':correo,'rol':rol,'talleres':talleres,'usuarios_disponibles':usuarios_disponibles}
    return render(request,'paginas/gestionTalleres.html',datos)

def nuevoTaller(request):
    form=FotoForm(request.POST, request.FILES)
    nombre=request.POST['nombre']
    admin=request.POST['administrador']
    direccion=request.POST['direccion']
    telefono=request.POST['telefono']
    errores=0
    if not form.is_valid():
        errores+=1
        messages.error(request,'Ingrese una foto')
    if len(nombre)<=3:
        errores+=1
        messages.error(request,'Ingrese un nombre valido')
    if admin=='null':
        errores+=1
        messages.error(request,'Seleccione un administrador')
    if len(direccion)<5:
        errores+=1
        messages.error(request,'Ingrese una dirección valida')
    if len(telefono)!=10:
        errores+=1
        messages.error(request,'Ingrese un telefono valido')
    if errores==0:
        form.save()#Guadro la foto
        foto=Foto.objects.all().last()
        urlFoto=str(foto.foto)
        print(f"Foto: {urlFoto}")
        Servi.crear_taller(admin,nombre,direccion,telefono,urlFoto)
        messages.success(request,'Tienda creada exitosamente')
    return redirect('gestionarTalleres')