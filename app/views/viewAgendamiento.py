from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from ..services import Servicios

Servi=Servicios()

def vistaAgendamiento(request):
    return render(request,'paginas/agendamiento.html')