from pydantic import BaseModel

class CampoAd(BaseModel):
    id:int
    campo:str
