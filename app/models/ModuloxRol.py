from pydantic import BaseModel

class Moduloxrol(BaseModel):
    id:int
    materia:str
    id_usuario:int
    estado:str