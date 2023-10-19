from fastapi import APIRouter
from controllers.estadisticas_controller import *
estadistica=APIRouter(prefix="/stadistics")

nueva_estadistica=EstadisticasController()

@estadistica.get('/contarTutorias')


def contarTutorias():
    rpta=nueva_estadistica.get_id()
    return rpta