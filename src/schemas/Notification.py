from pydantic import BaseModel
class Notification(BaseModel):
    id:int=None
    nombre:str=None
    apellido:str=None
    celular:int
    correo:str
    mensaje:str
    id_estado:int=None
    respuesta:str=None

class NotificationSend(BaseModel):
        id:int=None
        nombre:str=None
        apellido:str=None
        celular:int
        correo:str
        mensaje:str
        id_estado:int=None
        respuesta:str=None
        nombre_completo:str

