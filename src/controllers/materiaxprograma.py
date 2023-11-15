

import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.FpxMateria import FpxMateria, createFpxMateria, updateFpxMateria
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
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="programaxmateria not found")

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def creatematxpro(self,fpxmateria:createFpxMateria):
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
    def getMaterias(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
SELECT fpxm.id_fpxm,f.facultad,p.programa,m.materia FROM `fpxmateria` fpxm
join facultadxprograma fxp on fxp.id_fxp=fpxm.id_fxp
join facultades f on f.id_facultad=fxp.id_facultad
join programas p on p.id_programa=fxp.id_programa
join materias m on m.id_materia=fpxm.id_materia
""")
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'programa': data[1],
                    'facultad':data[2],
                    'materia':data[3]
                   

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="facultadxprogramaxmateria not found")

        except mysql.connector.Error as err:
            conn.rollback()
            
        finally:
            conn.close()


    def createMateria(self,materia:createFpxMateria):
        try:
            print(materia)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
select fxp.id_fxp from facultadxprograma fxp WHERE fxp.id_facultad=%s and fxp.id_programa=%s  



""",(materia.facultad,materia.programa))
            result=cursor.fetchone()
            print(result)
            cursor.execute(
                "INSERT INTO fpxmateria (id_fxp, id_materia) VALUES (%s,%s)", (result[0],materia.materia,))
            conn.commit()
            conn.close()
            return {"success": "programaxfacultadxmateria creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "programaxfacultadxmateria  ya existe en el programa"})
        finally:
            conn.close()

    def getMateriaForId(self,id:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT fpxm.id_fpxm,f.facultad,p.programa,m.materia FROM `fpxmateria` fpxm
join facultadxprograma fxp on fxp.id_fxp=fpxm.id_fxp
join facultades f on f.id_facultad=fxp.id_facultad
join programas p on p.id_programa=fxp.id_programa
join materias m on m.id_materia=fpxm.id_materia where fpxm.id_fpxm=%s
                           
""",(id,))
            data = cursor.fetchone()
            
           
            content = {
                    'id': data[0],
                    'programa': data[1],
                    'facultad':data[2],
                    'materia':data[3]
                   

                }
            print(content)
            if data:
                return content
            else:
                raise HTTPException(
                    status_code=404, detail="facultadxprogramaxmateria not found")

        except mysql.connector.Error as err:
            conn.rollback()
            
        finally:
            conn.close()

    def updateMateria(self,data:updateFpxMateria,id:int):
        try:
            print(data)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("select id_materia from materias where materia=%s",(data.materia,))
            id_materia=cursor.fetchone()[0]
            cursor.execute("""update fpxmateria set id_materia=%s
where id_fpxm=%s
                           
""",(id_materia,id,))
            conn.commit()
            conn.close()
            return {"success":"ha sido actualizada la materia"}

        except mysql.connector.Error as err:
            conn.rollback()
            return {"error":"ocurrio algun error"}
            
        finally:
            conn.close()

