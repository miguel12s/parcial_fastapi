from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from schemas.Materia import Materia
from config.db_config import get_db_connection
import mysql.connector

class ModelAdmin:
    def getMaterias():
        try:
            print('entras')
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM materias")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'materia': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="materia not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def getMateria(id_materia: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM materias WHERE id_materia= %s", (id_materia,))
            result = cursor.fetchone()
            if result:
                
                content = {}

                content = {
                    'id': int(result[0]),
                    'materia': result[1]
                }
                
                print(content)
                json_data = jsonable_encoder(content)
                print(json_data)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="materia not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def createMateria( materia: Materia):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO materias (materia) VALUES (%s)", (materia.materia,))
            conn.commit()
            conn.close()
            return {"resultado": "materia  creada"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "la materia  ya existe en el programa"})
        finally:
            conn.close()