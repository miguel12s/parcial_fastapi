from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    nombre: str
    apellido: str
    cedula: str
    edad: int
    usuario: str
    contrasena: str


