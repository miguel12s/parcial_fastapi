from fastapi import APIRouter
from typing import List
from controllers.tipoxestado_controller  import *
from schemas.TipoxEstado import TipoxEstado

tipoxestado=APIRouter()

nuevo_tipoxestado=TipoxEstadoController()

@tipoxestado.get('/tipoxestado',response_model=List[TipoxEstado])

def getTipoxEstado():
    rpta=nuevo_tipoxestado.getTipoxEstados()
    return rpta['resultado']



@tipoxestado.get('/tipoxestado-user',response_model=List[TipoxEstado])

def getTipoxEstadoForUser():
    rpta=nuevo_tipoxestado.getTipoxEstadosForUser()
    return rpta['resultado']

@tipoxestado.get('/tipoxestado/{id}',response_model=TipoxEstado)

def getTipoxEstado(id):
    rpta=nuevo_tipoxestado.getTipoxEstado(id)
    print(rpta)
    return rpta

@tipoxestado.post('/tipoxestado')

def createTipoxEstado(tipoxestado:TipoxEstado):
    rpta=nuevo_tipoxestado.createTipoxEstado(tipoxestado)
    return rpta


@tipoxestado.put('/tipoxestado/{id}')

def updateTipoxEstado(tipoxestado:TipoxEstado,id):
    rpta=nuevo_tipoxestado.updateTipoxEstado(tipoxestado,id)
    return rpta


