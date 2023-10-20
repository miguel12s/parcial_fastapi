from fastapi import APIRouter
from controllers.estadisticas_controller import *
estadistica=APIRouter(prefix="/stadistics")

nueva_estadistica=EstadisticasController()

@estadistica.get('/contar-usuarios')


def contarTutorias():
    rpta=nueva_estadistica.get_id()
    return rpta

@estadistica.get('/contar-tutorias')


def contarTutorias():
    rpta=nueva_estadistica.getTutorias()
    return rpta