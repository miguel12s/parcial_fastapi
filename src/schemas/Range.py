from pydantic import BaseModel

class Range(BaseModel):
     tipo_reporte:str
     fecha_inicio:str
     fecha_final:str