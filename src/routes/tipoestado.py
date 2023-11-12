from fastapi import APIRouter
from typing import List
from controllers.tipoestado import *
from schemas.TipoEstado import TipoEstado

tipoEstado=APIRouter()

nuevo_tipoEstado=TipoEstadoController()


@tipoEstado.get('/tipo_estado',response_model=List[TipoEstado])


def getTipoEstados():
      rpta=nuevo_tipoEstado.getTipoEstados()
      return rpta['resultado']

@tipoEstado.get('/tipo_estado/{id_tipo_estado}',response_model=TipoEstado)


def getTipoEstado(id_tipo_estado):
      rpta=nuevo_tipoEstado.getTipoEstado(id_tipo_estado)
      return rpta
@tipoEstado.post('/tipo_estado')

def createTipoEstado(tipo_estado:TipoEstado):
      rpta=nuevo_tipoEstado.createTipoEstado(tipo_estado)
      return rpta

@tipoEstado.put('/tipo_estado/{id}')

def updateTipoEstadoTipoEstado(tipo_estado:TipoEstado,id:int):
      rpta=nuevo_tipoEstado.updateTipoEstado(tipo_estado,id)
      return rpta


