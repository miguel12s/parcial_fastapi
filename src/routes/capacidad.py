from fastapi import APIRouter
from typing import List
from controllers.capacidad_controller import *
from schemas.Capacidad import Capacidad
capacidad=APIRouter()

nueva_capacidad=CapacidadController()


@capacidad.post('/capacidad',status_code=201)

async def createCapacidad(capacidad:Capacidad):
        rpta=nueva_capacidad.createCapacidad(capacidad)  
        return rpta

@capacidad.get('/capacidad',response_model=List[Capacidad])

async def getCapacidades():
        rpta=nueva_capacidad.getCapacidades()  
        return rpta['resultado']


@capacidad.get('/capacidad/{id_capacidad}',response_model=Capacidad)

async def getCapacidad(id_capacidad):
        rpta=nueva_capacidad.getCapacidad(id_capacidad)  
        return rpta


