from fastapi import APIRouter
from typing import List
from controllers.listado_estudiantes import *
from models.ListadoEstudiante import ListadoEstudiante
listado=APIRouter()

nueva_listado=ListadoController()


@listado.post('/listado',status_code=201)

async def createListado(horario:ListadoEstudiante):
        rpta=nueva_listado.createListado(horario)  
        return rpta

@listado.get('/listado',response_model=List[ListadoEstudiante])

async def getListados():
        rpta=nueva_listado.getListados()  
        return rpta['resultado']


@listado.get('/listado/{id}',response_model=ListadoEstudiante)

async def getListado(id_capacidad):
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
        


