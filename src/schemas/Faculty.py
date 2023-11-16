from pydantic import BaseModel

class Faculty(BaseModel):
    id:int=0
    facultad:str


class FacultyxUser(BaseModel):
    id_fpxusuario:int
    facultad:str
    programa:str
