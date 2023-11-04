from fastapi import APIRouter, Request,UploadFile
from typing import Any, List
from controllers.horario_controller import *
from schemas.Horario import Horario
from utils.Security import Security
horario=APIRouter()

nueva_horario=HorarioController()


@horario.post('/horario',status_code=201)

async def createHorario(horario:Horario,request:Request):
        headers=request.headers
        payload=Security.verify_token(headers)
        id_usuario=payload['id_usuario']
        rpta=nueva_horario.createHorario(horario,id_usuario)  
        return rpta

@horario.get('/horario')

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

@horario.get('/horario-usuario')

async def horarioUsuario(request:Request):
        headers=request.headers
        payload=Security.verify_token(headers)
        id_usuario=payload['id_usuario']
        rpta=nueva_horario.getHorarioForIdUsuario(id_usuario)
        return rpta

@horario.post('/observacion/{id_usuario}')

async def observacion(file:UploadFile,id_usuario):
        try: 
                rpta=await nueva_horario.createObservacion(file,id_usuario)
                return rpta
        except Exception as e:
                print(e)
                
                


