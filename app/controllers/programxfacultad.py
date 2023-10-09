import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.ProgramxFacultad import ProgramxFacultad
from fastapi.encoders import jsonable_encoder


class ProgramaFacultadController:
    def getFacultadxProgramas(self):
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
    def getFacultadxPrograma(self,id_fxp:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """select  fp.id_fxp, f.facultad,p.programa from facultadxprograma fp join facultades f on fp.id_facultad=f.id_facultad join programas p on fp.id_programa=p.id_programa where id_fxp=%s
""", (id_fxp,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                    'id': int(result[0]),
                    'facultad': result[1],
                    'programa':result[2]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="programa not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def createFacultadxPrograma(self,facultadxprograma:ProgramxFacultad):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
SELECT DISTINCT
    f.id_facultad,
    p.id_programa
FROM 
    facultades AS f
JOIN 
    facultadxprograma AS fxp ON f.facultad = %s
JOIN 
    programas AS p ON p.programa = %s;





""",(facultadxprograma.facultad,facultadxprograma.programa))
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