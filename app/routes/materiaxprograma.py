from fastapi import APIRouter
from typing import List
from controllers.materiaxprograma import *
from models.FpxMateria import FpxMateria
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



