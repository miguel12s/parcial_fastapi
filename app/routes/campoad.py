from fastapi import APIRouter
from typing import List
from controllers.campoad_controller import *
from schemas.CampoAd import CampoAd

campoad=APIRouter()

nuevo_campoad=CampoadController()


@campoad.get('/campoad',response_model=List[CampoAd])


def campoadf():
      rpta=nuevo_campoad.getCamposAd()
      return rpta['resultado']

@campoad.get('/campoad/{id_campo}',response_model=CampoAd)


def campoadg(id_campo):
      rpta=nuevo_campoad.getCampoAd(id_campo)
      return rpta
@campoad.post('/campoad')

def createCampoad(campo:CampoAd):
      rpta=nuevo_campoad.createCampoAd(campo)
      return rpta
