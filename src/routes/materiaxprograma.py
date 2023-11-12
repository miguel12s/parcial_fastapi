from fastapi import APIRouter
from typing import List
from controllers.materiaxprograma import *
from schemas.FpxMateria import FpxMateria,createFpxMateria, updateFpxMateria
from controllers.materiaxprograma import *

materiaxprograma=APIRouter()

nueva_materiaxprograma=MateriaProgramaController()


@materiaxprograma.get('/matxpro',response_model=List[FpxMateria])

def getMatxPros():
      rpta=nueva_materiaxprograma.getmatxpros()
      return rpta

@materiaxprograma.get('/matxpro/{id_facultad}/{id_programa}')

def getmatxpro(id_programa:str,id_facultad:str):
      
      rpta=nueva_materiaxprograma.getmatxprow(id_programa,id_facultad)
      print(rpta)
      return rpta

@materiaxprograma.post('/matxpro')

def creatematxpro(fxp:FpxMateria):
      rpta=nueva_materiaxprograma.creatematxpro(fxp)
      return rpta

@materiaxprograma.get('/materia-pro-fac')

def getMateria():
      rpta=nueva_materiaxprograma.getMaterias()
      return rpta


@materiaxprograma.post('/materia-pro-fac')

def createMateria(materia:createFpxMateria):
      rpta=nueva_materiaxprograma.createMateria(materia)
      return rpta

@materiaxprograma.get('/materia-pro-fac/{id}')

def getMateriaForId(id):
      rpta=nueva_materiaxprograma.getMateriaForId(id)
      return rpta

@materiaxprograma.put('/materia-pro-fac/{id}')

def getMateriaForId(data:updateFpxMateria,id:int):
      print(data)
      rpta=nueva_materiaxprograma.updateMateria(data,id)
      return rpta



