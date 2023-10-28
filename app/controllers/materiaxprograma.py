

import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.FpxMateria import FpxMateria
from fastapi.encoders import jsonable_encoder


class MateriaProgramaController:
    def getmatxpros(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
SELECT fp.id_fxp,p.programa, f.facultad FROM `facultadxprograma` fp join facultades f on fp.id_facultad=f.id_facultad join programas p on fp.id_programa=p.id_programa 
""")
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'programa': data[1],
                    'facultad':data[2]
                   

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="facultadxprograma not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def getmatxprow(self,id_programa:int,id_facultad:int):
        try:
            print('entras')
            conn = get_db_connection()
            cursor = conn.cursor()
            print(id_facultad,id_programa)
            cursor.execute(""" select m.id_materia, m.materia  from fpxmateria fpx join facultadxprograma fxp on fxp.id_fxp=fpx.id_fxp  join materias m on fpx.id_materia=m.id_materia where fpx.id_fxp=(select id_fxp from facultadxprograma fp where fp.id_facultad=%s and fp.id_programa=%s)""",(id_facultad,id_programa))
            
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}

            for data in result:
                content = {
                    'id': data[0],
                    'materia': data[1],                   

                }
                payload.append(content)
                content = {}
            print(result)
            json_data = jsonable_encoder(payload)
            print(result)            
            if result:
                print('enbtrs ')
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="programaxmateria not found")

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def creatematxpro(self,fpxmateria:FpxMateria):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
#             cursor.execute("""
# SELECT DISTINCT
#     f.id_facultad,
#     p.id_programa
# FROM 
#     facultades AS f
# JOIN 
#     facultadxprograma AS fxp ON f.facultad = %s
# JOIN 
#     programas AS p ON p.programa = %s;





# """,(facultadxprograma.facultad,facultadxprograma.programa))
            result=cursor.fetchone()
            print(result)
            cursor.execute(
                "INSERT INTO facultadxprograma (id_facultad,id_programa) VALUES (%s,%s)", (result[0],result[1],))
            conn.commit()
            conn.close()
            return {"resultado": "programaxfacultad creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "programaxfacultad  ya existe en el programa"})
        finally:
            conn.close()
