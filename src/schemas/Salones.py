from pydantic import BaseModel

class Salones(BaseModel):
    id_salon:int=0
    sede:str
    capacidad:int
    salon:str