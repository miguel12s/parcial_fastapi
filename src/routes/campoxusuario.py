from fastapi import APIRouter
from typing import List
from controllers.campoxusuario_controller import *
from schemas.CampoxUsuario import CampoxUsuario
campoxusuario=APIRouter()

nueva_campoxusuario=CampoxUsuarioController()


@campoxusuario.get('/campoxusuario',response_model=List[CampoxUsuario])

async def getCampoxUsuarios():
    rpta=nueva_campoxusuario.getCampoxUsuarios()
    return rpta['resultado']

@campoxusuario.get('/campoxusuario/{id}',response_model=CampoxUsuario)

async def getCampoxUsuario(id):
    rpta=nueva_campoxusuario.getCampoxUsuario(id)
    return rpta

@campoxusuario.post('/campoxusuario')

async def createCampoxUsuario(campoxusuario:CampoxUsuario):
    rpta=nueva_campoxusuario.createCampoxUsuario(campoxusuario)
    return rpta
