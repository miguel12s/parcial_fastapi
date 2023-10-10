from pydantic import BaseModel

class ListadoEstudiante(BaseModel):
    id:int
    id_horario:int
    id_usuario:int
    comentario:str
    asistencia:str