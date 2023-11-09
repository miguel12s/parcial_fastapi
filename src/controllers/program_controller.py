import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.Program import Program
from fastapi.encoders import jsonable_encoder

class ProgramaController:
    def getProgramas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
select * from programas
""")
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'programa': data[1],
                   

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="programa not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def getPrograma(self,id_programa:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM programas WHERE id_programa= %s", (id_programa,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                    'id': int(result[0]),
                    'programa': result[1]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="programa not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def createProgram(self,program:Program):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO programas (programa) VALUES (%s)", (program.programa,))
            conn.commit()
            conn.close()
            return {"success": "programa  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "el programa  ya existe en el programa"})
        finally:
            conn.close()
    def update_program(self,data:Program,id_program):
        try:
            print(id_program)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""update programas set programa=%s where id_programa=%s""",(data.programa,id_program))
            conn.commit()
            conn.close()
            return {"success":"el programa ha sido actualizada"}
            

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return {"error":"el programa se encuentra registrada en el programa"}
        finally:
            conn.close()
