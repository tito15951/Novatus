import requests

class Servicios:
    def __init__(self):
        self.dir="http://127.0.0.1:8000/api/"
    def iniciarSesion(self,correo,contrasena):
        dir=self.dir+"usuarios"
        datos={
            'login':"",
            'correo':correo,
            'contrasenia':contrasena
        }
        resp=requests.post(dir,datos)
        return resp.json()
    
    def registrarse(self,correo,nombre,contrasena):
        dir=self.dir+"usuarios"
        datos={
            'create':'',
            'correo':correo,
            'nombre':nombre,
            'contrasenia':contrasena,
        }
        resp=requests.post(dir,datos)
        return resp.json()
        
    #def registrarse(self,correo,contrasena,nombre, )