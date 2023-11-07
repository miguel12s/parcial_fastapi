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

@reporte.post('/horario/{id}')

def reporteHorarios(id,request:Request,data:Range):
    headers=request.headers
    payload=Security.verify_token(headers=headers)
    user_id=payload['id_usuario']
    rpta=nuevo_reporte.obtenerListadoPorHorario(user_id,id,data)
    return rpta
