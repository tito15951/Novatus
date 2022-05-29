from ..models import Servicio
from django.views import View
from django.http import JsonResponse

class Servi(View):
    def get(self,request):
        servicios=Servicio.objects.all().order_by('descripcion')
        servicios=list(servicios.values('descripcion'))
        return JsonResponse(servicios,safe=False,status=200)
    
    def post(self,request):
        descripcion=request.POST['descripcion']
        Servicio.objects.create(descripcion=descripcion)
        return JsonResponse({'resp':True},status=200,safe=False)
