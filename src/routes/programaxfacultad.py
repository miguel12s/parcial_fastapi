from fastapi import APIRouter
from typing import List
from controllers.programxfacultad import *
from schemas.ProgramxFacultad import ProgramxFacultad

programaxfacultad=APIRouter()

nueva_programaxfacultad=ProgramaFacultadController()


@programaxfacultad.get('/facultadxprograma',response_model=List[ProgramxFacultad])

def getFacultadxProgramas():
      rpta=nueva_programaxfacultad.getFacultadxProgramas()
      return rpta['resultado']

@programaxfacultad.get('/facxpro/{id_facultad}')

def getFacultadxPrograma(id_facultad:str):
      rpta=nueva_programaxfacultad.getFacultadxProgramaDesc(id_facultad)
      return rpta

@programaxfacultad.post('/facultadxprograma')

def createFacultadxPrograma(fxp:ProgramxFacultad):
      rpta=nueva_programaxfacultad.createFacultadxPrograma(fxp)
      return rpta

@programaxfacultad.put('/facultadxprograma/{id_fxp}')

def updateFacultadxPrograma(fxp:ProgramxFacultad,id_fxp:int):
      rpta=nueva_programaxfacultad.updateFacultadxPrograma(fxp,id_fxp)
      return rpta
@programaxfacultad.get('/facultadxprograma/{id_facultad}')

def getFacultadForPrograma(id_facultad):
       rpta=nueva_programaxfacultad.getFacultadxPrograma(id_facultad)
       return rpta



