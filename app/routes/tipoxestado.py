from fastapi import APIRouter
from typing import List
from controllers.tipoxestado_controller  import *
from models.TipoxEstado import TipoxEstado

tipoxestado=APIRouter()

nuevo_tipoxestado=TipoxEstadoController()

@tipoxestado.get('/tipoxestado',response_model=List[TipoxEstado])

def getTipoxEstado():
    rpta=nuevo_tipoxestado.getTipoxEstados()
    return rpta['resultado']

@tipoxestado.get('/tipoxestado/{id}',response_model=TipoxEstado)

def getTipoxEstado(id):
    rpta=nuevo_tipoxestado.getTipoxEstado(id)
    return rpta

@tipoxestado.post('/tipoxestado')

def createTipoxEstado(tipoxestado:TipoxEstado):
    rpta=nuevo_tipoxestado.createTipoxEstado(tipoxestado)
    return rpta


