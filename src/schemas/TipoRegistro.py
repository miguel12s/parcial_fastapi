from pydantic import BaseModel

class TipoRegistro(BaseModel):
    id:int=None
    tipoRegistro:str

 