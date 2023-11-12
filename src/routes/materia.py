from fastapi import APIRouter
from typing import List
from controllers.materia_controller import MateriaController
from schemas.Materia import Materia

materia=APIRouter()


@materia.get('/materia')

def materiaf():
      return MateriaController.getMaterias()

@materia.get('/materia/{id_materia}',response_model=Materia)

def materiag(id_materia:int):
      return MateriaController.getMateria(id_materia)
     

@materia.post('/materia')

def materiaw(materia:Materia):
      return MateriaController.createMateria(materia)


@materia.put('/materia/{id}')

def updateMateria(materia:Materia,id:int):
      return MateriaController.updateMateria(materia,id)

