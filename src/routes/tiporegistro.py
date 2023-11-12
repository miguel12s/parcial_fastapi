from fastapi import APIRouter
from typing import List
from controllers.tiporegistro_controller import *
from schemas.TipoRegistro import TipoRegistro

tipoRegistro=APIRouter()

nuevo_tipoRegistro=TipoRegistroController()


@tipoRegistro.get('/tipo_registro',response_model=List[TipoRegistro])


def getTipoRegistros():
      rpta=nuevo_tipoRegistro.getTipoRegistros()
      return rpta['resultado']

@tipoRegistro.get('/tipo_registro/{id_tipo}',response_model=TipoRegistro)


def getTipoRegistro(id_tipo):
      rpta=nuevo_tipoRegistro.getTipoRegistro(id_tipo)
      return rpta
@tipoRegistro.post('/tipo_registro')

def createTipoRegistro(tipo_registro:TipoRegistro):
      rpta=nuevo_tipoRegistro.createTipoRegistro(tipo_registro)
      return rpta

@tipoRegistro.put('/tipo_registro/{id}')

def createTipoRegistro(tipo_registro:TipoRegistro,id:int):
      rpta=nuevo_tipoRegistro.updateTipoRegistro(tipo_registro,id)
      return rpta
