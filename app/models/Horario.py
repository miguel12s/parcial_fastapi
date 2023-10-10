from pydantic import BaseModel
from datetime import date
class Horario(BaseModel):
    id:int
    facultad:str
    programa:str
    materia:str
    salon:str
    id_usuario:int
    estado_tutoria:str
    cupos:int
    tema:str
    fecha:date
    hora_inicial:str
    hora_final:str
