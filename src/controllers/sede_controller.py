import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.Sede import Sede
from fastapi.encoders import jsonable_encoder

class SedeController:
    def getSedes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sedes")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'sede': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Sede not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def getSede(self, id_sede: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sedes WHERE id_sede= %s", (id_sede,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                    'id': int(result[0]),
                    'sede': result[1]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Sede not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def createSede(self, sede: Sede):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO sedes (sede) VALUES (%s)", (sede.sede,))
            conn.commit()
            conn.close()
            return {"success": "sede  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "la sede  ya existe en el programa"})
        finally:
            conn.close()
    def update_sede(self,data:Sede,id_sede):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""update sedes set sede=%s where id_sede=%s""",(data.sede,id_sede))
            conn.commit()
            conn.close()
            return {"success":"la sede ha sido actualizada"}
            

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return {"error":"la sede se encuentra registrada en el programa"}
        finally:
            conn.close()