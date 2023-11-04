import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.CampoAd import CampoAd
from fastapi.encoders import jsonable_encoder

class CampoadController:
    def getCamposAd(self):
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM campoad")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'campo': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="campo not found")

         except mysql.connector.Error as err:
            conn.rollback()
         finally:
            conn.close()

    def getCampoAd(self, id_campo: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM campoad WHERE id_campo= %s", (id_campo,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                    'id': int(result[0]),
                    'campo': result[1]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="campo not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def createCampoAd(self, campo: CampoAd):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO campoad (campo) VALUES (%s)", (campo.campo,))
            conn.commit()
            conn.close()
            return {"resultado": "campo  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "el campo  ya existe en el programa"})
        finally:
            conn.close()
