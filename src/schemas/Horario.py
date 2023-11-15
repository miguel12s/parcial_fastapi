from pydantic import BaseModel
from datetime import date
class Horario(BaseModel):
    id:int=None
    id_facultad:int
    id_programa:str
    id_materia:str
    id_salon:int
    id_capacidad:int
    id_sede:str
    id_estado_tutoria:str="4"
    cupos:int
    tema:str
    fecha:date
    hora_inicial:str
    hora_final:str

class Horariof(BaseModel):
    id:int=None
    id_facultad:int
    id_programa:int
    id_materia:str
    id_salon:str
    id_capacidad:int
    id_sede:str
    id_estado_tutoria:str="4"
    cupos:int
    tema:str
    fecha:date
    hora_inicial:str
    hora_final:str
class  AgendarTutoria(BaseModel):
    id:int