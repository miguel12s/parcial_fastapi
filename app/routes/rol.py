from fastapi import APIRouter
from typing import List
from controllers.rol_controller import *
from models.Rol import Rol

rol=APIRouter()

nuevo_rol=RolController()


@rol.get('/roles',response_model=List[Rol])


def rolesf():
      rpta=nuevo_rol.getRoles()
      return rpta['resultado']

@rol.get('/roles/{id_rol}',response_model=Rol)


def rolesg(id_rol):
      rpta=nuevo_rol.getRol(id_rol)
      return rpta
@rol.post('/roles')

def createRoles(rol:Rol):
      rpta=nuevo_rol.createRol(rol)
      return rpta
