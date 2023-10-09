from fastapi import APIRouter
from typing import List
from controllers.programxfacultad import *
from models.ProgramxFacultad import ProgramxFacultad

programaxfacultad=APIRouter()

nueva_programaxfacultad=ProgramaFacultadController()


@programaxfacultad.get('/facultadxprograma',response_model=List[ProgramxFacultad])

def getFacultadxProgramas():
      rpta=nueva_programaxfacultad.getFacultadxProgramas()
      return rpta['resultado']

@programaxfacultad.get('/facultadxprograma/{id_fxp}',response_model=ProgramxFacultad)

def getFacultadxPrograma(id_fxp):
      rpta=nueva_programaxfacultad.getFacultadxPrograma(id_fxp)
      return rpta

@programaxfacultad.post('/facultadxprograma')

def createFacultadxPrograma(fxp:ProgramxFacultad):
      rpta=nueva_programaxfacultad.createFacultadxPrograma(fxp)
      return rpta

