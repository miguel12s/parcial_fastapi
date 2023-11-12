from pydantic import BaseModel


class TipoxEstado(BaseModel):
    id:int=None
    tipoxestado:str
    estado:str