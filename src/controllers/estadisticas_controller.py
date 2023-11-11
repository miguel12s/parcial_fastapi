import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder

class EstadisticasController():
    def get_id(self):
         conn = get_db_connection()
         cursor = conn.cursor()
         cursor.execute('SELECT count(case when id_rol=1 then 1 else null end) as estudiantes , COUNT(CASE WHEN id_rol=2 THEN 1 ELSE NULL END) AS docentes from usuarios ')
         cantidades=cursor.fetchone()
         content={"estudiante":cantidades[0],
                  "docente":cantidades[1]
                  }   
         json_data=jsonable_encoder(content)
         return json_data
    def getTutorias(self):
          conn = get_db_connection()
          cursor = conn.cursor()
          cursor.execute("""SELECT
    YEAR(ht.fecha) AS año,
    MONTH(ht.fecha) AS mes,

    SUM(CASE WHEN txe.id_tipoxestado=6 THEN 1 ELSE 0 END) AS tutorias_terminadas,
    SUM(CASE WHEN txe.id_tipoxestado=8 THEN 1 ELSE 0 END) AS tutorias_eliminadas
FROM horario_tutorias ht 
join tipoxestado txe on txe.id_tipoxestado=ht.id_estado_tutoria
GROUP BY año,mes
ORDER BY año,mes""")
          cantidades=cursor.fetchall()
          payload=[]
          for data in cantidades:
               content={
                    "año":data[0],
                    "mes":data[1],
                    "tutorias_terminadas":int(data[2]),
                    "tutorias_eliminadas":int(data[3])
               }

               payload.append(content)
               content={}
         
          json_data=jsonable_encoder(payload)
          return json_data

         
    

