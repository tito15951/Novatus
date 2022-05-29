from django.shortcuts import render, redirect
from ..services import Servicios
from django.contrib import messages
Servi=Servicios()
from datetime import datetime
from datetime import timedelta
def viewCrearAgendamiento(request):
    hoy=datetime.now()
    conversor=timedelta(hours=-5)
    hoy=hoy+conversor
    hoy=hoy.strftime('%Y-%m-%d')
    id=request.POST['id']
    taller=Servi.buscar_taller(id)
    servicios=Servi.obtener_servicios()
    #print(taller)
    id_taller=taller['id']
    #print(f"el id del taller es: {id_taller}")
    #servicios=["Cambio de aceite","Cambio de llanta"]
    marcas=["Susuki","Yamaha","Honda"]
    correo=request.session['correo']
    rol=request.session['rol']
    nombre_taller=f"{taller['nombre']}-{taller['direccion']}"
    datos={"servicios":servicios,"correo":correo,"rol":rol,"marcas":marcas,'taller':nombre_taller,'fecha':hoy,'id_taller':id_taller}
    return render(request,'paginas/crearAgendamiento.html',datos)

def CrearAgendamiento(request):
    taller=request.POST['id_taller']
    usuario=request.session['correo']
    hora=request.POST['hora']
    fecha=request.POST['calendario']
    descripcion=request.POST['servicio']
    placa_moto=request.POST['placa']
    if(len(placa_moto)<5):
        messages.error(request,'Ingrese la placa de la moto')
        return redirect('crearAgendamiento')
    Servi.crea_cita(taller,usuario,f"{fecha} {hora}",descripcion,placa_moto.upper())
    return redirect('misAgendamientos')
    ##print(f"Se creará una cita al taller #{taller} para el usuario {usuario} en la fecha {fecha} {hora} a la moto {placa_moto} por {descripcion}")