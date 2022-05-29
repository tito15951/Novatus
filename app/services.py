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
    
    #                TALLERES
    def listar_talleres(self):
        dir=self.dir+'talleres?listar'
        resp=requests.get(dir)
        return resp.json()

    def listar_citas_taller(self,correo_duenio):
        dir=self.dir+'citas?listar_tienda='+str(correo_duenio)
        resp=requests.get(dir)
        return resp.json()

    def listar_citas_usuario(self,correo_usuario):
        dir=self.dir+'citas?listar_cliente='+str(correo_usuario)
        resp=requests.get(dir)
        return resp.json()

    
    def buscar_taller(self,id):
        dir=self.dir+'talleres?listar_id='+str(id)
        resp=requests.get(dir)
        return resp.json()

    #              CHAT
    def buscar_mensajes(self,cita):
        dir=self.dir+'chat?cita='+str(cita)
        resp=requests.get(dir)
        return resp.json()

    def nuevo_mensaje(self,origen,destino,mensaje,cita):
        dir=self.dir+'chat'
        datos={
            'nuevo':'',
            'destino':destino,
            'origen':origen,
            'cita':cita,
            'mensaje':mensaje
        }
        resp=requests.post(dir,datos)
        return resp.json()

    #              COMENTARIOs
    def nuevo_comentario(self,escritor,valoracion,tienda,cita):
        dir=self.dir+'comentarios'
        datos={
            'crear_comentario':'',
            'id_usuario':escritor,
            'id_tienda':tienda,
            'puntuacion':valoracion,
            'cita':cita
        }
        resp=requests.post(dir,datos)
        return resp.json()
    #def registrarse(self,correo,contrasena,nombre, )