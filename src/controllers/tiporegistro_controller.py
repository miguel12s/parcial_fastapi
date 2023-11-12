import mysql.connector
from fastapi import HTTPException
from schemas.TipoRegistro import TipoRegistro
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder

class TipoRegistroController:


    def getTipoRegistros(self):
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipo_registro_actividad")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'tipoRegistro': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="tipo del registro not found")

         except mysql.connector.Error as err:
            conn.rollback()
         finally:
            conn.close()

    def getTipoRegistro(self, id_tipo_actividad: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM tipo_registro_actividad WHERE id_tipo_actividad= %s", (id_tipo_actividad,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                    'id': int(result[0]),
                    'tipoRegistro': result[1]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="tipo registro not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def createTipoRegistro(self, tipoRegistro: TipoRegistro):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tipo_registro_actividad (tipo_actividad) VALUES (%s)", (tipoRegistro.tipoRegistro,))
            conn.commit()
            conn.close()
            return {"success": "tipo registro  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "el tipo registro  ya existe en el programa"})
        finally:
            conn.close()
    def updateTipoRegistro(self, tipoRegistro: TipoRegistro,id:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "update tipo_registro_actividad set tipo_actividad=%s where id_tipo_actividad=%s", (tipoRegistro.tipoRegistro,id))
            conn.commit()
            conn.close()
            return {"success": "tipo registro  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "el tipo registro  ya existe en el programa"})
        finally:
            conn.close()