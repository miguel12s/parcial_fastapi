from pydantic import BaseModel

class ProgramxFacultad(BaseModel):
    id:int=0
    programa:str
    facultad:str    
