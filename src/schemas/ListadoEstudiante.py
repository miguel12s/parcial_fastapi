from pydantic import BaseModel

class ListadoEstudiante(BaseModel):
    id:int=0
    
    id_usuario:int
    asistencia:bool
    id_tutoria:int
    observacion:str
