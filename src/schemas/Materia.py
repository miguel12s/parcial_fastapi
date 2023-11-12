from pydantic import BaseModel

class Materia(BaseModel):
    id:int=0
    materia:str

