from fastapi import APIRouter, Request,UploadFile
from typing import Any, List
from controllers.horario_controller import *
from schemas.Horario import Horario,AgendarTutoria,Horariof
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

@horario.post('/horario-admin/{id_usuario}')

async def createHorario(horario:Horariof,id_usuario):
        print(horario)
        rpta=nueva_horario.createHorario(horario,id_usuario)  
        return rpta

@horario.get('/horario')

async def getHorarios():
        rpta=nueva_horario.getHorarios()  
        return rpta['resultado']


@horario.get('/horario/{id}')

async def getHorario(id:int):
        print(id)
        rpta=nueva_horario.getHorario(id)  
        return rpta

@horario.put('/horario/{id}')

async def updateHorario(horario:Horario,id:int):
        rpta=nueva_horario.updateHorario(horario,id)
        return rpta

@horario.delete('/horario/{id}')

async def deleteHorario(id,request:Request):
        headers=request.headers
        payload=Security.verify_token(headers)
        id_usuario=payload['id_usuario']
        rpta=nueva_horario.deleteHorario(id,id_usuario)
        return rpta

@horario.delete('/horario/eliminar-tutoria/{id_tutoria}/{id_usuario}')

async def deleteHorario(id_tutoria,id_usuario):
        rpta=nueva_horario.deleteHorarioAdmin(id_tutoria,id_usuario)
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
                
@horario.post('/agendar')

def agendarTutoria(tutoria:AgendarTutoria,request:Request):
    try:
        headers=request.headers
        payload=Security.verify_token(headers)
        user_id=payload['id_usuario']
        rpta=nueva_horario.agendarTutoria(tutoria.id,user_id)
        return rpta
    except Exception as e :
        print(e)
        raise HTTPException(status_code=400,detail=e) 
@horario.get('/mostrarTutoriasEstudiante')

def mostrarTutoriasEstudiante(request:Request):
    try:
        headers=request.headers
        payload=Security.verify_token(headers)
        user_id=payload['id_usuario']
        rpta=nueva_horario.obtenerTutoriasPendientes(user_id)
        return rpta
    except Exception as e :
        print(e)
        raise HTTPException(status_code=400,detail=e) 
    
@horario.get('/obtenerTutoriaFinalizadas')

def obtenerTutoriaFinalizadas(request:Request):
    try:
        headers=request.headers
        payload=Security.verify_token(headers)
        user_id=payload['id_usuario']
        rpta=nueva_horario.obtenerTutoriaFinalizada(user_id)
        return rpta
    except Exception as e :
        print(e)
        raise HTTPException(status_code=400,detail=e) 


@horario.get('/obtenerTutoriaFinalizadasDocente')

def obtenerTutoriaFinalizadaDocente(request:Request):
    try:
        headers=request.headers
        payload=Security.verify_token(headers)
        user_id=payload['id_usuario']
        rpta=nueva_horario.obtenerTutoriaFinalizadaDocente(user_id)
        return rpta
    except Exception as e :
        print(e)
        raise HTTPException(status_code=400,detail=e) 



@horario.delete('/cancelarTutoria/{id_tutoria}')

def cancelarTutoria(request:Request,id_tutoria:int):
      try:
        headers=request.headers
        payload=Security.verify_token(headers)
        user_id=payload['id_usuario']
        rpta=nueva_horario.cancelarTutoria(user_id,id_tutoria)
        return rpta
      except Exception as e :
        print(e)
        raise HTTPException(status_code=400,detail=e)

    

@horario.get('/horario-terminado')

def obtenerTutoriaFinalizadass():
    try:
        rpta=nueva_horario.obtenerTutoriaFinalizadass()
        return rpta
    except Exception as e :
        print(e)
        raise HTTPException(status_code=400,detail=e) 
               
        


