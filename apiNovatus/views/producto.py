from ..models import Producto
from django.views import View
from django.http import JsonResponse

class Product(View):
    def get(self,request):
        if('listar' in request.GET):
            product=Producto.objects.all()
            return JsonResponse(list(product.values('id','nombre')),safe=False,status=200)
        else:
            return JsonResponse({'Resp':'No implementado'},safe=False,status=404)
