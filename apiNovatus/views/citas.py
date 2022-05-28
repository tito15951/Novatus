from ..models import Cita, Comentario, Tienda, Usuario 
from django.views import View
from django.http import JsonResponse

class mostrar_citas(View):
    def get(self,request):
        if ('listar_tienda' in request.GET):
            correo=request.GET['listar_tienda']
            try:
                usuario=Usuario.objects.get(correo=correo)
                tienda=Tienda.objects.get(admin=usuario)
                citas=Cita.objects.filter(id_tienda=tienda).order_by('-id')
                return JsonResponse(list(citas.values()),status=200,safe=False)
            except:
                return JsonResponse({'resp':False},status=404,safe=False)
        elif 'listar_cliente' in request.GET:
            correo=request.GET['listar_cliente']
            try:
                usuario=Usuario.objects.get(correo=correo)
                citas=Cita.objects.filter(id_usuario=usuario).order_by('-id')
                return JsonResponse(list(citas.values()),status=200,safe=False)
            except:
                return JsonResponse({'resp':False},status=404,safe=False)
        elif('listar' in request.GET):
            Mostrar_citas=Cita.objects.all()
            return JsonResponse(list(Mostrar_citas.values('id','id_tienda','id_usuario','hora', 'descripcion', 'placa_moto')),safe=False,status=200)
        elif('listar_id' in request.GET):
            if('id' in request.GET):
                idRequest=request.GET['id']
                cita=Cita.objects.filter(id=idRequest)
                return JsonResponse(list(cita.values('id','id_tienda','id_usuario','hora', 'descripcion', 'placa_moto')),safe=False,status=200)
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)


    def post(self, request):
        if('crear_cita' in request.POST):
            if(('id_tienda' in request.POST) and ('id_usuario' in request.POST) and ('hora' in request.POST) and ('descripcion' in request.POST) and ('placa_moto' in request.POST) ):
                try:
                    id_tiendaRequest=request.POST['id_tienda']
                    id_usuarioRequest=request.POST['id_usuario']
                    horaRequest=request.POST['hora']
                    descripcionRequest=request.POST['descripcion']
                    placa_motoRequest=request.POST['placa_moto']
                    id_usuario=Usuario.objects.filter(correo=id_usuarioRequest).first()
                    id_tienda=Tienda.objects.filter(id=id_tiendaRequest).first()
                except:
                    return JsonResponse({'Resp1':False},safe=False,status=400)
                try:
                    newcita=Cita.objects.create(hora=horaRequest,
                                                descripcion=descripcionRequest,
                                                placa_moto=placa_motoRequest,
                                                id_usuario=id_usuario,
                                                id_tienda=id_tienda)
                    return JsonResponse({'Resp2':True},safe=False,status=201)
                except:
                    return JsonResponse({'Resp3':False},safe=False,status=400)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)
        elif 'finalizar' in request.POST:
            try:
                cita=request.POST['finalizar']
                cita=Cita.objects.filter(id=cita).update(estado='finalizada')
                return JsonResponse({'Resp':True},safe=False,status=200)
            except:
                return JsonResponse({'Resp':False},safe=False,status=200)
        elif('update' in request.POST):
            if(('id_tienda' in request.POST) and ('hora' in request.POST) and ('descripcion' in request.POST) and ('placa_moto' in request.POST) ):
                try:
                    idRequest=request.POST['id']
                    id_tiendaRequest=request.POST['id_tienda']
                    horaRequest=request.POST['hora']
                    descripcionRequest=request.POST['descripcion']
                    placa_motoRequest=request.POST['placa_moto']
                    id=Cita.objects.filter(id=idRequest).first()
                except:
                    return JsonResponse({'Resp1':False},safe=False,status=400)
                citas=Cita.objects.filter(id=idRequest).update(id_tienda=id_tiendaRequest,
                                            hora=horaRequest,
                                            descripcion=descripcionRequest,
                                            placa_moto=placa_motoRequest)                    
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
        
