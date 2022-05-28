from django.db import models

# Create your models here.
class Usuario(models.Model):
    correo=models.EmailField(primary_key=True)
    nombre=models.TextField(max_length=30,null=False)
    contrasenia=models.TextField(max_length=20,null=False)
    direccion=models.TextField(max_length=20,null=True)
    telefono=models.TextField(max_length=10,null=True)
    rol=models.TextField(max_length=10,null=False,default='cliente')
    def __str__(self):
        return self.nombre+'-'+self.correo+'-'+self.rol

class Tienda(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre=models.TextField(max_length=20,null=False)
    admin=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    direccion=models.TextField(max_length=20,null=False)
    valoracion=models.IntegerField(default=0, null=False)
    tel=models.TextField(max_length=10,null=False)

    def __str__(self):
        return self.nombre+'-'+self.admin.nombre

class Cita(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_tienda=models.ForeignKey(Tienda,on_delete=models.CASCADE)
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    hora=models.TextField(default="Sin hora")
    duracion=models.IntegerField(null=False,default=0)
    descripcion=models.TextField(max_length=200,null=False)
    placa_moto=models.TextField(max_length=6,null=False,default="")

    def __str__(self):
        return str(self.id)+'-'+self.id_usuario.correo+' '+str(self.hora)+' '+self.id_tienda.nombre

class Comentario(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_tienda=models.ForeignKey(Tienda,on_delete=models.CASCADE,null=True)
    puntuacion=models.IntegerField(null=False,default=0)
    def __str__(self):
        return str(self.id)+' '+str(self.id_usuario.correo)+' '


class Chat(models.Model):
    id=models.BigAutoField(primary_key=True)
    cita=models.ForeignKey(Cita,on_delete=models.CASCADE,default="")
    origen=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="origen")
    destino=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="destino")
    mensaje=models.TextField(max_length=150)
    hora=models.DateTimeField(null=True,auto_now=True)
    def __str__(self):
        return f"{self.id}-{self.origen.correo}->{self.destino.correo}: {self.mensaje[:10]}"
        
class MedioPago(models.Model):
    id=models.BigAutoField(primary_key=True)
    num_tarjeta=models.TextField(max_length=16,null=False)
    cod_seguridad=models.TextField(max_length=3,null=False)
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha_venc=models.TextField(max_length=5,null=False)
    def __str__(self):
        return str(self.id_usuario.correo)+'-****'+str(self.num_tarjeta[-4:])