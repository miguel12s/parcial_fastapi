import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.Capacidad import Capacidad
from fastapi.encoders import jsonable_encoder

class CapacidadController:
    
    def getCapacidades(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM capacidades")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'capacidad': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="capacidad not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def getCapacidad(self, id_capacidad: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM capacidades WHERE id_capacidad= %s", (id_capacidad,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                    'id': int(result[0]),
                    'capacidad': result[1]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="Capacidad not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def createCapacidad(self, capacidad: Capacidad):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO capacidades (capacidad) VALUES (%s)", (capacidad.capacidad,))
            conn.commit()
            conn.close()
            return {"success": "capacidad  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "la capacidad  ya existe en el programa"})
        finally:
            conn.close()
    def update_capacidad(self,data:Capacidad,id_capacidad):
        try:
           
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""update capacidades set capacidad=%s where id_capacidad=%s""",(data.capacidad,id_capacidad))
            conn.commit()
            conn.close()
            return {"success":"la capacidad ha sido actualizada"}
            

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return {"error":"la capacidad se encuentra registrada en el programa"}
        finally:
            conn.close()
    
