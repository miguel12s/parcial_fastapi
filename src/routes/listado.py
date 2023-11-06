from fastapi import APIRouter, Request
from typing import List
from controllers.listado_estudiantes import *
from schemas.ListadoEstudiante import ListadoEstudiante
from utils.Security import Security
listado=APIRouter()

nueva_listado=ListadoController()


@listado.post('/listado',status_code=201)

async def createListado(listado:ListadoEstudiante):
        rpta=nueva_listado.createListado(listado)  
        return rpta

@listado.get('/listado',response_model=List[ListadoEstudiante])

async def getListados():
        rpta=nueva_listado.getListados()  
        return rpta['resultado']


@listado.get('/listado/{id}')

async def getListado(id):
        rpta=nueva_listado.getListado(id)  
        return rpta

@listado.put('/listado/{id}')

async def updateListado(listado:ListadoEstudiante,id:int):
        rpta=nueva_listado.updateListado(listado,id)
        return rpta

@listado.delete('/listado/{id}')

async def deleteListado(id):
        rpta=nueva_listado.deleteListado(id)
        return rpta

@listado.put('/pasar-lista')

async def pasarLista(request:Request,listado:List[ListadoEstudiante]):
    headers=request.headers
    payload=Security.verify_token(headers)
    user_id=payload['id_usuario']
    print(user_id)
    rpta = nueva_listado.pasarLista(user_id,listado)
    return rpta


        


