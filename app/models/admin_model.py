from pydantic import BaseModel



class Program(BaseModel):
    id:int
    programa:str
    facultad:str

class Faculty(BaseModel):
    id:int
    facultad:str

class typeDocument(BaseModel):
    id:int
    typeDocument:str

