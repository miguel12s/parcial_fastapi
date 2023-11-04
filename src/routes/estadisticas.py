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

@estadistica.get('/contar-usuarios-total')

def contarUsuariosTotal():
    rpta=nueva_estadistica.contarUsuariosTotal()
    return rpta

@estadistica.get('/contar-usuarios-hoy')

def contarUsuariosHoy():
    rpta=nueva_estadistica.contarUsuariosHoy()
    return rpta


@estadistica.get('/contar-tutorias-totales')

def contarUsuariosHoy():
    rpta=nueva_estadistica.contarTutoriasTotales()
    return rpta

@estadistica.get('/obtener-notificaciones')

def contarNotificaciones():
    rpta=nueva_estadistica.contarTutoriasTotales()
    return rpta



