from pydantic import BaseModel


class TipoEstado(BaseModel):
    id:int=None
    tipoEstado:str