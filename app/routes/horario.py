from fastapi import APIRouter
from typing import List
from controllers.horario_controller import *
from models.Horario import Horario
horario=APIRouter()

nueva_horario=HorarioController()


@horario.post('/horario',status_code=201)

async def createHorario(horario:Horario):
        rpta=nueva_horario.createHorario(horario)  
        return rpta

@horario.get('/horario',response_model=List[Horario])

async def getHorarios():
        rpta=nueva_horario.getHorarios()  
        return rpta['resultado']


@horario.get('/horario/{id}',response_model=Horario)

async def getHorario(id:int):
        rpta=nueva_horario.getHorario(id)  
        return rpta

@horario.put('/horario/{id}')

async def updateHorario(horario:Horario,id:int):
        rpta=nueva_horario.updateHorario(horario,id)
        return rpta

@horario.delete('/horario/{id}')

async def deleteHorario(id):
        rpta=nueva_horario.deleteHorario(id)
        return rpta
        


