from fastapi import APIRouter
from typing import List
from controllers.sede_controller import *
from schemas.Sede import Sede
sede=APIRouter()

nueva_sede=SedeController()


@sede.post('/sede',status_code=201)

async def createSede(sede:Sede):
        rpta=nueva_sede.createSede(sede)  
        return rpta

@sede.get('/sede',response_model=List[Sede])

async def getSedes():
        rpta=nueva_sede.getSedes()  
        return rpta['resultado']


@sede.get('/sede/{id_sede}',response_model=Sede)

async def getSede(id_sede):
        rpta=nueva_sede.getSede(id_sede)  
        return rpta

@sede.put("/sede/{id_sede}")
async def create_faculty(sede:Sede,id_sede):
    rpta = nueva_sede.update_sede(sede,id_sede)
    return rpta

