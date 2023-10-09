from pydantic import BaseModel


class TipoEstado(BaseModel):
    id:int
    tipoEstado:str