from pydantic import BaseModel



class Program(BaseModel):
    id:int
    programa:str
    facultad:str

class Faculty(BaseModel):
    id:int
    facultad:str

class TypeDocument(BaseModel):
    id:int
    tipo_documento:str

class Sede(BaseModel):
    id:int
    sede:str


class Capacidad(BaseModel):
    id:int
    capacidad:int

