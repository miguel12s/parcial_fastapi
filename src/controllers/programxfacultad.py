import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.ProgramxFacultad import FacultadxUsuario, ProgramxFacultad
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
    def getFacultadxPrograma(self,id_facultad:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT id_fxp,p.programa,f.facultad,p.id_programa FROM facultadxprograma fxp join programas p on fxp.id_programa=p.id_programa join facultades f  on f.id_facultad=fxp.id_facultad where fxp.id_facultad=%s
""", (id_facultad,))
            result = cursor.fetchall()
            payload=[]
            for data in result:
             content = {
                    'id': data[0],
                    'programa': data[1],
                    'id_programa':data[3]


                }
             payload.append(content)
             content={}
            json_data=jsonable_encoder(payload)
            print(json_data)

            if data:
                return {"resultado":json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="facultadxprograma not found")

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
            return {"success": "programaxfacultad creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "programaxfacultad  ya existe en el programa"})
        finally:
            conn.close()
    def updateFacultadxPrograma(self,data:ProgramxFacultad,id_fxp):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            print(data)
            cursor.execute("""SELECT p.id_programa,f.id_facultad from programas p join facultades f on f.facultad=%s
            where p.programa=%s
                           """,(data.facultad,data.programa))
            result=cursor.fetchone()
            print(result)
            cursor.execute("""update facultadxprograma  set id_facultad=%s,id_programa=%s where id_fxp=%s
                          
                            """,(result[1],result[0],id_fxp))
            conn.commit()
            conn.close()
            return {"success":"la facultadxprograma  ha sido actualizada"}
            

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return {"error":"la facultadxprograma  se encuentra registrada en el programa"}
        finally:
            conn.close()
    def getFacultadxProgramaDesc(self,id_fxp:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT id_fxp,p.programa,f.facultad FROM facultadxprograma fxp join programas p on fxp.id_programa=p.id_programa join facultades f  on f.id_facultad=fxp.id_facultad where fxp.id_fxp=%s
""", (id_fxp,))
            data= cursor.fetchone()
            
            content = {
                    'id': data[0],
                    'programa': data[1],
                    'facultad':data[2]


                }
            if data:
                return {"resultado":content}
            else:
                raise HTTPException(
                    status_code=404, detail="facultadxprograma not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def getProgramas(self,facultad:str):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            facultad.strip()
            new_faculty=facultad.strip()
            cursor.execute("""
SELECT p.programa FROM `facultadxprograma` fxp
join programas p on p.id_programa=fxp.id_programa

WHERE fxp.id_facultad=(select id_facultad from facultades where facultad=%s) 
""",(new_faculty,))
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                content = {
                    'programa': data[0],
                    

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
    def createFacultadxUsuario(self,facultad:FacultadxUsuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
select id_fxp from facultadxprograma fxp where fxp.id_facultad=(select id_facultad from facultades f  where f.facultad=%s) and fxp.id_programa=(select id_programa from programas p where p.programa=%s)





""",(facultad.facultad,facultad.programa))
            result=cursor.fetchone()[0]
            print(result)
            cursor.execute(
                "INSERT INTO `fpxusuario`( `id_fxp`, `id_usuario`) VALUES (%s,%s)", (result,facultad.id_usuario,))
            conn.commit()
            conn.close()
            return {"success": "facultadxusuario creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "programaxfacultad  ya existe en el programa"})
        finally:
            conn.close()