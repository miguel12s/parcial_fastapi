from pydantic import BaseModel,EmailStr
class User(BaseModel):
    id: int=None
    id_rol:int
    id_estado:int=1
    nombres: str
    apellidos: str
    id_tipo_documento:int
    numero_documento:int
    celular: str
    id_facultad:int
    id_programa:int
    foto:str=None
    correo:EmailStr
    contraseña:str

class updateUser(BaseModel):
    id: int=None
    estado:str
    nombres: str
    apellidos: str
    tipo_documento:str
    numero_documento:int
    celular: int
    facultad:str
    programa:str
    correo:EmailStr


