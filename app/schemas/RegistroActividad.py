from pydantic import BaseModel
from datetime import date
class RegistroActividad(BaseModel):
    id:int
    tipo_actividad:str
    id_usuario:int
    fecha:date
    hora:str
    ubicacion_actividad:str