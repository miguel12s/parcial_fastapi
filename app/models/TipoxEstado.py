from pydantic import BaseModel


class TipoxEstado(BaseModel):
    id:int
    tipoxestado:str
    estado:str