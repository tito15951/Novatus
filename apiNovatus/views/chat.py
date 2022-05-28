from ..models import Chat, Cita, Tienda,Usuario
from django.views import View
from django.http import JsonResponse

class Conversacion(View):
    def get(self,request):
        if 'listar' in request.GET:
            chats=Chat.objects.all()
            return JsonResponse(list(chats.values()),safe=False,status=200)
        elif 'cita' in request.GET:
            cita=Cita.objects.filter(id=request.GET['cita'])
            cita=list(cita.values())[0]
            usuario=Usuario.objects.filter(correo=cita['id_usuario_id'])
            usuario=list(usuario.values('correo'))[0]
            tienda=Tienda.objects.filter(id=cita['id_tienda_id'])
            tienda=list(tienda.values('admin_id','nombre'))[0]
            chats=Chat.objects.filter(cita=request.GET['cita']).order_by('hora')
            info={'tienda':tienda['admin_id'],'usuario':usuario['correo'],'tienda_nombre':tienda['nombre'],'chats':list(chats.values())}
            return JsonResponse(info,safe=False,status=200)
        else:
            return JsonResponse({'resp':"No implementado"},safe=False,status=200)

    def post(self,request):
        if 'nuevo' in request.POST:
            if (('destino' in request.POST) and
                ('origen' in request.POST) and
                ('cita' in request.POST) and
                ('mensaje' in request.POST)):
                try:
                    origen=Usuario.objects.get(correo=request.POST['origen'])
                    destino=Usuario.objects.get(correo=request.POST['destino'])
                    cita=Cita.objects.get(id=request.POST['cita'])
                    mensaje=request.POST['mensaje']
                    Chat.objects.create(
                        cita=cita,
                        origen=origen,
                        destino=destino,
                        mensaje=mensaje
                    )
                    #print(f"El mensaje: {mensaje}, lo envia: {origen} para {destino} y es de la cita {cita}")
                    return JsonResponse({'resp':True},safe=False,status=200)
                except:
                    return JsonResponse({'resp':False},safe=False,status=200)