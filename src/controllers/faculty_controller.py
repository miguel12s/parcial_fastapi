import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.Faculty import Faculty, FacultyxUser
from fastapi.encoders import jsonable_encoder


class FacultyController:
    def create_faculty(self, facultad: Faculty):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO facultades (facultad) VALUES (%s)", (facultad.facultad,))
            conn.commit()
            conn.close()
            return {"resultado": "facultad creada"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "la facultad ya existe en el programa"})
        finally:
            conn.close()

    def get_faculty(self, id_facultad: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM facultades WHERE id_facultad = %s", (id_facultad,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                    'id': int(result[0]),
                    'facultad': result[1]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="Type Document not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_faculties(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM facultades")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'facultad': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="Programs not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def get_faculty_user(self,id_user):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT DISTINCT f.id_facultad, f.facultad from fpxusuario fu join facultadxprograma fxp on fxp.id_fxp=fu.id_fxp join facultades f on f.id_facultad=fxp.id_facultad where fu.id_usuario=%s""",(id_user,))
            result = cursor.fetchall()
            payload = []
            content = {}
            print(result)
            for data in result:
                content = {
                    'id': data[0],
                    'facultad': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="Programs not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def update_faculty(self,data:Faculty,id_faculty):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""update facultades set facultad=%s where id_facultad=%s""",(data.facultad,id_faculty))
            conn.commit()
            conn.close()
            return {"success":"la facultad ha sido actualizada"}
            

        except mysql.connector.Error as err:
            
            conn.rollback()
            return {"error":"la facultad se encuentra registrada en el programa"}
        finally:
            conn.close()
    def getFacultadUserDocente(self,id_usuario:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT DISTINCT f.id_facultad, f.facultad from fpxusuario fu join facultadxprograma fxp on fxp.id_fxp=fu.id_fxp join facultades f on f.id_facultad=fxp.id_facultad where fu.id_usuario=%s """,(id_usuario,))
            result = cursor.fetchall()
            payload = []
            content = {}
            print(result)
            for data in result:
                content = {
                    'id': data[0],
                    'facultad': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="Programs not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def getFacultadUser(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT  fpx.id_fpxusuario,concat(u.nombres,' ',u.apellidos),u.id_usuario as nombre_completo FROM `fpxusuario` fpx 
join facultadxprograma fxp on fxp.id_fxp=fpx.id_fxp
join facultades f on f.id_facultad=fxp.id_facultad
join programas p on fxp.id_programa=p.id_programa
join usuarios u on fpx.id_usuario=u.id_usuario
group by u.id_usuario
    """)
            # group by u.id_usuario
            result = cursor.fetchall()
           
            payload = []
            content = {}
            for data in result:
                    print(data)
                    content = {
                        'id': data[0],
                        'nombre_completo': data[1],
                        'id_usuario':data[2]
                    }
                    payload.append(content)
                    content={}

            json_data = jsonable_encoder(payload)
            return json_data
           
                

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def getFacultadxUsuario(self,id_usuario:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT p.programa,f.facultad,fpx.id_fpxusuario FROM `fpxusuario` fpx
join facultadxprograma fxp on fxp.id_fxp=fpx.id_fxp
join facultades f on f.id_facultad=fxp.id_facultad
join programas p on p.id_programa=fxp.id_programa
where fpx.id_usuario=%s """,(id_usuario,))
            result = cursor.fetchall()
            payload=[]
            content={}
            for data in result:
                content = {
                        'programa': data[0],
                        'facultad': data[1],
                        'id':data[2]
                    }
                payload.append(content)
                content={}
            print(payload)
            json_data=jsonable_encoder(payload)
            if result:
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="Programs not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def getFacultadxUsuarioForId(self,id_fpxusuario:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT concat(u.nombres,' ',u.apellidos) as nombre_completo, p.programa,f.facultad,u.id_usuario,fpx.id_fpxusuario FROM `fpxusuario` fpx
join facultadxprograma fxp on fxp.id_fxp=fpx.id_fxp
join facultades f on f.id_facultad=fxp.id_facultad
join programas p on p.id_programa=fxp.id_programa
join usuarios u on u.id_usuario=fpx.id_usuario
where fpx.id_fpxusuario=%s """,(id_fpxusuario,))
            result = cursor.fetchone()
            
            content = {
                    'nombre_completo':result[0],
                        'programa': result[1],
                        'facultad': result[2],
                        'id_usuario':result[3],
                        'id':result[4]

                    }
            print(content)
            if result:
                return content
            else:
                raise HTTPException(
                    status_code=404, detail="Programs not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def updateFacultadxUsuarioForId(self,id_fpxusuario:int,data:FacultyxUser):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""select id_fxp from facultadxprograma where id_facultad=(select id_facultad from facultades where facultad=%s) and id_programa=(select id_programa from programas where programa=%s) """,(data.facultad,data.programa))
            result = cursor.fetchone()
            print(result)
            print
            
            cursor.execute("""
UPDATE `fpxusuario` SET id_fxp=%s WHERE id_fpxusuario=%s
""",(result[0],id_fpxusuario))
            conn.commit()

            conn.close()
            return {"success":"el usuario ha sido actualizado"}

        except (Exception) as err:
            conn.rollback()
            return {"error":"la facultad y el programa que desea modificar no carecen de sentido"}
        finally:
            conn.close()