from pydantic import BaseModel


class ChangePassword(BaseModel):
    contraseña_actual:str
    contraseña_nueva:str