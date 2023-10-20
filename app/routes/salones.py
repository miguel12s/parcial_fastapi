from fastapi import APIRouter
from typing import List
from controllers.salones_controller import *
from models.Salones import Salones

salones=APIRouter()

nuevo_salon=SalonesController()

@salones.post('/salones')

def create_salones(salones:Salones):
      rpta=nuevo_salon.create_salones(salones)
      return rpta

@salones.get('/salones')
def get_salones():
      rpta=nuevo_salon.get_salones()
      return rpta

@salones.get('/salones/{id_salon}',response_model=Salones)

def get_salones(id_salon):
      rpta=nuevo_salon.get_salonesid(id_salon)
      return rpta