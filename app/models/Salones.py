from pydantic import BaseModel

class Salones(BaseModel):
    id_salon:int
    sede:str
    capacidad:int
    salon:str