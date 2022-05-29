from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()

def vistaChat(request):
    correo=request.session['correo']
    rol=request.session['rol']
    cita=request.POST['id']
    info=Servi.buscar_mensajes(cita)
    chats=info['chats']
    request.session['tienda']=info['tienda']
    request.session['usuario']=info['usuario']
    request.session['cita']=cita
    datos={"correo":correo,'rol':rol,'chats':chats,'cita':cita,'nombre_tienda':info['tienda_nombre']}
    return render(request,'paginas/chat.html',datos)

def nuevoMensaje(request):

    mensaje=request.POST['mensaje']
    correo_origen=request.session['correo']
    tienda=request.session['tienda']
    usuario=request.session['usuario']
    cita=request.session['cita']
    if mensaje !='':
        del request.session['tienda']
        del request.session['usuario']
        del request.session['cita']
        if tienda==correo_origen:
            origen=tienda
            destino=usuario
        else:
            origen=usuario
            destino=tienda
        Servi.nuevo_mensaje(origen,destino,mensaje,cita)
        if request.session['rol']=='tienda':
            return redirect('citasTienda')
        else:
            return redirect('misAgendamientos')