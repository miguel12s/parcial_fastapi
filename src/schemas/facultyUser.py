from pydantic import BaseModel

class FacultyUser(BaseModel):
    id:int
    capacidad:int
