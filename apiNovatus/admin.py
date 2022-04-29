from django.contrib import admin
from .models import Categoria, Cita, Comentario, Compra, Factura, MedioPago, Producto, Tienda, Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Comentario)
admin.site.register(Tienda)
admin.site.register(Cita)
admin.site.register(MedioPago)
admin.site.register(Compra)
admin.site.register(Factura)