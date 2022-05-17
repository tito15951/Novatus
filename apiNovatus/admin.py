from django.contrib import admin
from .models import Cita, Comentario, MedioPago, Tienda, Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Tienda)
admin.site.register(Cita)
admin.site.register(MedioPago)