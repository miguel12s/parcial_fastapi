from pydantic import BaseModel

class Faculty(BaseModel):
    id:int=0
    facultad:str
