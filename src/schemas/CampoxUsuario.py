from pydantic import BaseModel
class CampoxUsuario(BaseModel):
    id:int
    id_usuario:int
    campo:str
    dato:str