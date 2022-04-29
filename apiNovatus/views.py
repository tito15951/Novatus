from asyncio.windows_events import NULL
from django.shortcuts import render
from .models import Usuario, Producto
from django.views import View
from django.http import JsonResponse

class Product(View):
    def get(self,request):
        if('listar' in request.GET):
            product=Producto.objects.all()
            return JsonResponse(list(product.values('id','nombre')),safe=False,status=200)
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)

# Create your views here.
class User(View):
    def get(self,request):
        if('listar' in request.GET):
            users=Usuario.objects.all()
            return JsonResponse(list(users.values('correo','nombre')),safe=False,status=200)
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)


    def post(self,request):
        if('login' in request.POST):
            if(('correo' in request.POST) and ('contrasenia' in request.POST)):
                correoRequest=request.POST['correo']
                contraseniaRequest=request.POST['contrasenia']
                user=Usuario.objects.filter(correo=correoRequest, contrasenia=contraseniaRequest)
                if(user.count()>0):
                    return JsonResponse({'Resp':'Logeado correctamente'},safe=False,status=200)
                else:
                    return JsonResponse({'Resp':'Error al iniciar sesion'},safe=False,status=200)
            else:
                return JsonResponse({'Resp':'Faltan datos'},safe=False,status=400)


        elif('create' in request.POST):
            if(('correo' in request.POST) and ('nombre' in request.POST) and ('contrasenia' in request.POST)):
                try:
                    correoRequest=request.POST['correo']
                    nombreRequest=request.POST['nombre']
                    contraseniaRequest=request.POST['contrasenia']
                except:
                    return JsonResponse({'Resp':'Faltan datos'},safe=False,status=400)
                try:
                    newUser=Usuario.objects.create(correo=correoRequest,nombre=nombreRequest,contrasenia=contraseniaRequest)
                    return JsonResponse({'Resp':'Creado exitosamente'},safe=False,status=201)
                except:
                    return JsonResponse({'Resp':'Error al crear el usuario'},safe=False,status=202)
            else:
                return JsonResponse({'Resp':'Faltan datos'},safe=False,status=400)
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)
