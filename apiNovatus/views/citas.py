from ..models import Cita, Tienda, Usuario
from django.views import View
from django.http import JsonResponse

class Citas(View):
    def get(self,request):
        if 'listar' in request.GET:
            citas=Cita.objects.filter(id_usuario_id=request.GET['listar'])
            return JsonResponse(list(citas.values()),safe=False,status=200)
        else:
            return JsonResponse(status=404)
