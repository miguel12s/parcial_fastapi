from fastapi import APIRouter
from typing import List
from controllers.program_controller import *
from schemas.Program import Program

programa=APIRouter()

nueva_programa=ProgramaController()

@programa.get('/programa',response_model=List[Program])

def programaf():
      rpta=nueva_programa.getProgramas()
      return rpta['resultado']

@programa.get('/programa/{id_programa}',response_model=Program)

def getPrograma(id_programa):
      rpta=nueva_programa.getPrograma(id_programa)
      return rpta

@programa.post('/programa')

def createPrograma(program:Program):
      rpta=nueva_programa.createProgram(program)
      return rpta


@programa.put("/programa/{id_programa}")
async def create_faculty(programa:Program,id_programa):
    rpta = nueva_programa.update_program(programa,id_programa)
    return rpta