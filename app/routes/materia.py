from fastapi import APIRouter
from typing import List
from controllers.materia_controller import *
from models.Materia import Materia

materia=APIRouter()

nueva_materia=MateriaController()

@materia.get('/materia',response_model=List[Materia])

def materiaf():
      rpta=nueva_materia.getMaterias()
      return rpta['resultado']

@materia.get('/materia/{id_materia}',response_model=Materia)

def materiag(id_materia):
      rpta=nueva_materia.getMateria(id_materia)
      return rpta

@materia.post('/materia')

def materiaw(materia:Materia):
      rpta=nueva_materia.createMateria(materia)
      return rpta

