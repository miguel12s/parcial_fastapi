from fastapi import APIRouter, Request
from typing import List
from controllers.reporte_controller import *
from schemas.Range import Range
from utils.Security import Security


reporte=APIRouter(prefix='/reporte')

nuevo_reporte=ReporteController()


@reporte.post('/usuarios')
def reporteListadoEstudiante(data:Range):
    rpta=nuevo_reporte.obtenerListadoEstudiantes(data)
    return rpta

@reporte.get('/horario/{id}')

def reporteHorarios(id):
    rpta=nuevo_reporte.obtenerListadoPorHorario(id)
    return rpta
