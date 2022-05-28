from ..models import Usuario 
from django.views import View
from django.http import JsonResponse

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
                    return JsonResponse({'Resp':True,'rol':user.first().rol},safe=False,status=200)
                else:
                    return JsonResponse({'Resp':False},safe=False,status=200)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)


        elif('create' in request.POST):
            if(('correo' in request.POST) and 
                ('nombre' in request.POST) and 
                ('contrasenia' in request.POST)):
                try:
                    correoRequest=request.POST['correo']
                    nombreRequest=request.POST['nombre']
                    contraseniaRequest=request.POST['contrasenia']
                except:
                    return JsonResponse({'Resp':False},safe=False,status=400)
                try:
                    newUser=Usuario.objects.create(correo=correoRequest,
                                                nombre=nombreRequest,
                                                contrasenia=contraseniaRequest,
                                                rol="usuario",
                                                direccion="nulo",
                                                telefono="nulo")
                    return JsonResponse({'Resp':True},safe=False,status=201)
                except:
                    return JsonResponse({'Resp':False},safe=False,status=202)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)
