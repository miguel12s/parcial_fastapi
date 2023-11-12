from fastapi import APIRouter
from typing import List
from controllers.rol_controller import *
from schemas.Rol import Rol

rol=APIRouter()

nuevo_rol=RolController()


@rol.get('/roles')


def rolesf():
      rpta=nuevo_rol.getRoles()
      return rpta

@rol.get('/roles/{id_rol}',response_model=Rol)


def rolesg(id_rol):
      rpta=nuevo_rol.getRol(id_rol)
      return rpta
@rol.post('/roles')

def createRoles(rol:Rol):
      rpta=nuevo_rol.createRol(rol)
      return rpta

@rol.put('/roles/{id}')

def updateRoles(rol:Rol,id:int):
      rpta=nuevo_rol.updateRol(rol,id)
      return rpta

