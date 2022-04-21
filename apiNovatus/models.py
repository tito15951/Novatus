from django.db import models

# Create your models here.
class Usuario(models.Model):
    correo=models.EmailField(primary_key=True)
    nombre=models.TextField(max_length=30,null=False)
    contrasenia=models.TextField(max_length=20,null=False)

    def __str__(self):
        return self.nombre


