from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios
Servi=Servicios()

def viewCrearAgendamiento(request):
    return render(request,'paginas/crearAgendamiento.html')