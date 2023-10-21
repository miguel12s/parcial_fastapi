from fastapi import APIRouter,UploadFile
from typing import Any, List
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


@horario.get('/horario/{id}')

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

@horario.get('/horario-usuario/{id}')

def horarioUsuario(id):
        rpta=nueva_horario.getHorarioForIdUsuario(id)
        return rpta

@horario.post('/observacion/{id_usuario}')

async def observacion(file:UploadFile,id_usuario): 
        rpta=await nueva_horario.createObservacion(file,id_usuario)
        return rpta
        


