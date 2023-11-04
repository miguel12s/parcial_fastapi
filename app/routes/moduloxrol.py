from fastapi import APIRouter
from typing import List
from controllers.moduloxrol import *
from schemas.ModuloxRol import Moduloxrol

moduloxrol=APIRouter()

nueva_moduloxrol=ModuloxRolController()


@moduloxrol.get('/moduloxrole',response_model=List[Moduloxrol])

def getModulosxRol():
    rpta=nueva_moduloxrol.getModulosxRol()
    return rpta['resultado']

@moduloxrol.get('/moduloxrol/{id}',response_model=Moduloxrol)

def getModuloxRol(id):
    rpta=nueva_moduloxrol.getModuloxRol(id)
    return rpta

@moduloxrol.post('/moduloxrol')
def createModuloxRol(moduloxrol:Moduloxrol):
    rpta=nueva_moduloxrol.createModuloxRol(moduloxrol)
    return rpta