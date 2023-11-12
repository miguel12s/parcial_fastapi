from pydantic import BaseModel

class FpxMateria(BaseModel):
    id_fpxm:int
    id_fxp:int
    id_materia:int

class createFpxMateria(BaseModel):
    id_fpxm:int=0
    facultad:int
    programa:int
    materia:int

class updateFpxMateria(BaseModel):
    id_fpxm:int=0
    facultad:str
    programa:str
    materia:str