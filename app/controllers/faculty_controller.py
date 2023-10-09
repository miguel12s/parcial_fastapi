import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.Faculty import Faculty
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
