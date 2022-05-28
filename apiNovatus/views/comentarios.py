from apiNovatus.views.usuario import User
from ..models import Comentario, Tienda, Usuario 
from django.views import View
from django.http import JsonResponse

class mostrar_comentarios(View):
    def get(self,request):
        if('listar' in request.GET):
            MostrarComentarios=Comentario.objects.all()
            return JsonResponse(list(MostrarComentarios.values('id','id_usuario','id_tienda','puntuacion')),safe=False,status=200)
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)


    def post(self, request):
        if('crear_comentario' in request.POST):
            if(('id_usuario' in request.POST) and ('id_tienda' in request.POST) and ('puntuacion' in request.POST)):
                try:
                    id_usuarioRequest=request.POST['id_usuario']
                    id_tiendaRequest=request.POST['id_tienda']
                    puntuacionRequest=request.POST['puntuacion']
                    id_usuario=Usuario.objects.filter(correo=id_usuarioRequest).first()
                    id_tienda=Tienda.objects.filter(id=id_tiendaRequest).first()
                except:
                    return JsonResponse({'Resp1':False},safe=False,status=400)
                try:
                    newcomentario=Comentario.objects.create(id_usuario=id_usuario,
                                                id_tienda=id_tienda,
                                                puntuacion=puntuacionRequest)
                    
                    comentarios_tienda=Comentario.objects.filter(id_tienda=id_tiendaRequest)
                    puntuacion=0
                    contador = 0

                    for comentario in comentarios_tienda:

                        puntuacion=comentario.puntuacion+puntuacion
                        contador +=1
                        
                    resultado = puntuacion/contador

                    taller=Tienda.objects.filter(id=id_tiendaRequest).update(valoracion= resultado)

                    return JsonResponse({'Resp':True},safe=False,status=201)
                except:
                   return JsonResponse({'Resp':False},safe=False,status=400)
            else:
                return JsonResponse({'Resp':False},safe=False,status=400)
    

        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)
