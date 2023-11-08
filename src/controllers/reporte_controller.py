import mysql.connector
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from models.ModelReport import ModelReport
from schemas.Range import Range
class ReporteController:
   def obtenerListadoEstudiantes(self,data):
       try:
          rpta=ModelReport.obtenerListadoEstudiantes(data)
          return rpta
       except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)
   def obtenerListadoPorHorario(self,id):
    try:
          rpta=ModelReport.obtenerListadoPorHorario(id)
          return rpta
    except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)
