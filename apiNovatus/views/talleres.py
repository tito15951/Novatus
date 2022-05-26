from turtle import update
from requests import request
from apiNovatus.views.usuario import User
from ..models import Tienda, Usuario 
from django.views import View
from django.http import JsonResponse

class workshops(View):
    def get(self,request):
        if('listar' in request.GET):
            Talleres=Tienda.objects.all()
            return JsonResponse(list(Talleres.values('valoracion','nombre','direccion','tel')),safe=False,status=200)
        elif('listar_id' in request.GET):
            if('id' in request.GET):
                idRequest=request.GET['id']
                taller=Tienda.objects.filter(id=idRequest)
                return JsonResponse(list(taller.values('valoracion','nombre','direccion','tel')),safe=False,status=200)

        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)
        

    
    
    def post(self, request):
         if('crear_taller' in request.POST):
             if(('nombre' in request.POST) and ('admin' in request.POST) and ('direccion' in request.POST) and ('tel' in request.POST) ):
                try:
                    nombreRequest=request.POST['nombre']
                    adminRequest=request.POST['admin']
                    direccionRequest=request.POST['direccion']
                    telRequest=request.POST['tel']
                    admin=Usuario.objects.filter(correo=adminRequest).first()
                except:
                    return JsonResponse({'Resp':False},safe=False,status=400)
                try:
                    newtaller=Tienda.objects.create(nombre=nombreRequest,
                                                admin=admin,
                                                direccion=direccionRequest,
                                                tel=telRequest)
                    return JsonResponse({'Resp':True},safe=False,status=201)
                except:
                    return JsonResponse({'Resp':False},safe=False,status=400)
             else:
                return JsonResponse({'Resp':False},safe=False,status=400)
         elif('update' in request.POST):

             if(('id' in request.POST) and ('nombre' in request.POST) and ('admin' in request.POST) and ('direccion' in request.POST) and ('tel' in request.POST) ):
                try:
                    idRequest=request.POST['id']
                    nombreRequest=request.POST['nombre']
                    adminRequest=request.POST['admin']
                    direccionRequest=request.POST['direccion']
                    telRequest=request.POST['tel']
                    admin=Usuario.objects.filter(correo=adminRequest).first()
                except:
                    return JsonResponse({'Resp1':False},safe=False,status=400)
            
                taller=Tienda.objects.filter(id=idRequest).update(nombre=nombreRequest,
                                            admin=adminRequest,
                                            direccion=direccionRequest,
                                            tel=telRequest)
                                            
                return JsonResponse({'Resp':True},safe=False,status=200)

                
             else:
                 
                    return JsonResponse({'Resp3':False},safe=False,status=400)

         elif('delete' in request.POST):

             if('id' in request.POST):
                try:
                    idRequest=request.POST['id']
                except:
                    return JsonResponse({'Resp1':False},safe=False,status=400)
            
                Tienda.objects.filter(id=idRequest).delete()
                                            
                return JsonResponse({'Resp':True},safe=False,status=200)

                
             else:
                 
                    return JsonResponse({'Resp3':False},safe=False,status=400)


         else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)
        
         


    
            