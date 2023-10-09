from pydantic import BaseModel

class User(BaseModel):
    id: int
    id_rol:str
    id_estado:str
    nombre: str
    apellido: str
    tipo_documento:str
    numero_documento: str
    celular: str
    facultad:str
    foto:str
    correo:str
    contraseña:str


