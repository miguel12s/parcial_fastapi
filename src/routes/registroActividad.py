from fastapi import APIRouter
from typing import List
from controllers.registro_actividad import *
from schemas.RegistroActividad import RegistroActividad

registro_actividad=APIRouter()

nueva_registro_actividad=RegistroActividadController()


@registro_actividad.get('/registro_actividad')

def getRegistrosActividad():
    rpta=nueva_registro_actividad.getRegistrosActividad()
    return rpta

@registro_actividad.get('/registro_actividad/{id}',response_model=RegistroActividad)

def getRegistroActividad(id):
    rpta=nueva_registro_actividad.getRegistroActividad(id)
    return rpta

@registro_actividad.post('/registro_actividad')
def createRegistroActividad(registroactividad:RegistroActividad):
    rpta=nueva_registro_actividad.createRegistroActividad(registroactividad)
    return rpta