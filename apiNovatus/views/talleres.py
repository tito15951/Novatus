from ..models import Tienda, Usuario 
from django.views import View
from django.http import JsonResponse

class workshops(View):
    def get(self,request):
        if('listar' in request.GET):
            Talleres=Tienda.objects.all()
            return JsonResponse(list(Talleres.values('valoracion','nombre','direccion','tel')),safe=False,status=200)
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)

