from django.shortcuts import render, redirect
from ..services import Servicios
Servi=Servicios()
from datetime import datetime

def viewCrearAgendamiento(request):
    hoy=datetime.now()
    print(hoy)
    hoy=hoy.strftime('%Y-%m-%d')
    print(hoy)
    id=request.POST['id']
    taller=Servi.buscar_taller(id)
    servicios=["Cambio de aceite","Cambio de llanta"]
    marcas=["Susuki","Yamaha","Honda"]
    correo=request.session['correo']
    rol=request.session['rol']
    nombre_taller=f"{taller['nombre']}-{taller['direccion']}"
    datos={"servicios":servicios,"correo":correo,"rol":rol,"marcas":marcas,'taller':nombre_taller,'fecha':hoy}
    return render(request,'paginas/crearAgendamiento.html',datos)