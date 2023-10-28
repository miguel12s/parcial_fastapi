from pydantic import BaseModel
from datetime import date
class Horario(BaseModel):
    id:int=None
    id_facultad:str
    id_programa:str
    id_materia:str
    id_salon:str
    id_capacidad:str
    id_sede:str
    id_estado_tutoria:str
    cupos:int
    tema:str
    fecha:date
    hora_inicial:str
    hora_final:str
