from pydantic import BaseModel
class Notification(BaseModel):
    id:int=None
    nombre:str
    apellido:str
    celular:int
    correo:str
    mensaje:str
