import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.Rol import Rol
from fastapi.encoders import jsonable_encoder

class RolController:
    def getRoles(self):
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'rol': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="rol not found")

         except mysql.connector.Error as err:
            conn.rollback()
         finally:
            conn.close()

    def getRol(self, id_rol: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM roles WHERE id_rol= %s", (id_rol,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                    'id': int(result[0]),
                    'rol': result[1]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="Rol not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def createRol(self, rol: Rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO roles (rol) VALUES (%s)", (rol.rol,))
            conn.commit()
            conn.close()
            return {"success": "rol  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "el rol  ya existe en el programa"})
        finally:
            conn.close()
    def updateRol(self,rol:Rol,id:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "update roles set rol=%s where id_rol=%s",(rol.rol,id))
            conn.commit()
            conn.close()
            return {"success": "el rol ha sido actualizado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return {"error": "el rol  ya existe en el programa"}
        finally:
            conn.close()