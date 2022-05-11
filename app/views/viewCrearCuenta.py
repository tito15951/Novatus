from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
#from ..services import Servicios

def VistaCrearCuenta(request):
    marcas=["Kawasaki","Honda","Kymco","Susuki"]
    marcas.sort()
    print(marcas)
    datos={'marcas':marcas}
    return render(request,'paginas/crearCuenta.html',datos)