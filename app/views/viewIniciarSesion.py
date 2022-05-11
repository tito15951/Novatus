from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import sessions
from django.http import HttpResponse, HttpResponseRedirect
#from ..services import Servicios

def vistaLogin(request):
    return render(request,'paginas/inisiarSesion.html')