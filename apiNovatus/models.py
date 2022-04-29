from pyexpat import model
from statistics import mode
from unicodedata import category
from django.db import models

# Create your models here.
class Usuario(models.Model):
    correo=models.EmailField(primary_key=True)
    id=models.TextField(max_length=15,null=True)
    nombre=models.TextField(max_length=30,null=False)
    contrasenia=models.TextField(max_length=20,null=False)
    direccion=models.TextField(max_length=20,null=False)
    telefono=models.TextField(max_length=10,null=True)
    rol=models.TextField(max_length=10,null=False)

    def __str__(self):
        return self.nombre+'-'+self.correo+'-'+self.rol

class Categoria(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre=models.TextField(max_length=20,null=False)
    def __str__(self):
        return str(self.id)+'-'+self.nombre

class Producto(models.Model):
    id=models.BigAutoField(primary_key=True)
    marca=models.TextField(max_length=20,null=False)
    nombre=models.TextField(max_length=40,null=False)
    valor=models.IntegerField(null=False)
    descripcion=models.TextField(max_length=200,null=False)
    ref_moto=models.TextField(max_length=20,null=False)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    vendedor=models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.ref_moto+'-'+self.nombre

class Comentario(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    opinion=models.TextField(max_length=200,null=False)

    def __str__(self):
        return str(self.id)+' '+str(self.id_usuario.correo)+' '+self.id_producto.nombre

class Tienda(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre=models.TextField(max_length=20,null=False)
    admin=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    direccion=models.TextField(max_length=20,null=False)
    ciudad=models.TextField(max_length=20,null=False)
    tel=models.TextField(max_length=10,null=False)

    def __str__(self):
        return self.nombre+'-'+self.admin.nombre

class Cita(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_tienda=models.ForeignKey(Tienda,on_delete=models.CASCADE)
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    hora=models.DateTimeField(null=False)
    descripcion=models.TextField(max_length=200,null=False)

    def __str__(self):
        return self.id_usuario.correo+' '+str(self.hora)+' '+self.id_tienda.nombre
        
class MedioPago(models.Model):
    id=models.BigAutoField(primary_key=True)
    num_tarjeta=models.TextField(max_length=16,null=False)
    cod_seguridad=models.TextField(max_length=3,null=False)
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha_venc=models.TextField(max_length=5,null=False)

    def __str__(self):
        return str(self.id_usuario.correo)+'-****'+str(self.num_tarjeta[-4:])

class Compra(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_cliente=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    medioPago=models.ForeignKey(MedioPago,on_delete=models.CASCADE)
    valor=models.IntegerField(null=False)

    def __str__(self):
        return str(self.id)+' '+str(self.valor)

class Factura(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_compra=models.ForeignKey(Compra,on_delete=models.CASCADE)
    id_producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.IntegerField(null=False)
    valor=models.IntegerField(null=False)





