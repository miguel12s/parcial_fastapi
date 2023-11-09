from fastapi import APIRouter
from controllers.salones_controller import *
from schemas.Salones import Salones

salones=APIRouter()

nuevo_salon=SalonesController()

@salones.post('/salones')

def create_salones(salones:Salones):
      rpta=nuevo_salon.create_salones(salones)
      return rpta

@salones.get('/salones')
def get_salones():
      rpta=nuevo_salon.get_salones()
      return rpta['resultado']

@salones.get('/salones/{id_salon}',response_model=Salones)

def get_salones(id_salon):
      rpta=nuevo_salon.get_salonesid(id_salon)
      return rpta

@salones.put("/salones/{id_capacidad}")
async def create_faculty(salones:Salones,id_capacidad):
    rpta = nuevo_salon.update_salon(salones,id_capacidad)
    return rpta