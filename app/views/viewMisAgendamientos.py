from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()


def viewMisAgendamientos(request):
    correo=request.session['correo']
    citas=Servi.listar_citas_usuario(correo)
    #print(f"\n\n{citas}")
    rol=request.session['rol']
    datos={'correo':correo,'rol':rol,'citas':citas}
    return render(request,'paginas/misAgendamientos.html',datos)

def nuevoComentario(request):
    tienda=request.POST['tienda']
    usuario=request.session['correo']
    puntuacion=request.POST['puntuacion']
    cita=request.POST['cita_recibo']
    Servi.nuevo_comentario(usuario,puntuacion,tienda,cita)
    #print(f"El nuevo comentario es para la tienda: {tienda}, la valoracion fue: {puntuacion} y la hizo: {usuario} a la cita {cita}")
    return redirect('misAgendamientos')