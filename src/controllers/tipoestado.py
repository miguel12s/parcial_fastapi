import mysql.connector
from fastapi import HTTPException
from schemas.TipoEstado import TipoEstado
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder


class TipoEstadoController:
    def getTipoEstados(self):
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipoestado")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'tipoEstado': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="tipo del estado not found")

         except mysql.connector.Error as err:
            conn.rollback()
         finally:
            conn.close()

    def getTipoEstado(self, id_tipo_estado: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM tipoestado WHERE id_tipoestado= %s", (id_tipo_estado,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                    'id': int(result[0]),
                    'tipoEstado': result[1]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="tipo estado not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def createTipoEstado(self, tipoEstado: TipoEstado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tipoestado (tipo_estado) VALUES (%s)", (tipoEstado.tipoEstado,))
            conn.commit()
            conn.close()
            return {"success": "tipo estado  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "el tipo estado  ya existe en el programa"})
        finally:
            conn.close()
    def updateTipoEstado(self, tipoxestado: TipoEstado,id:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("update tipoestado set tipo_estado=%s where id_tipoestado=%s ", (tipoxestado.tipoEstado,id))
            conn.commit()
            conn.close()
            return {"success": "tipoxestado creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "tipoxestado  ya existe en el programa"})
        finally:
            conn.close()