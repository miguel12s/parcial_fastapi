import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.Salones import Salones
from fastapi.encoders import jsonable_encoder

class SalonesController:
    def get_salones(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT ds.id_salon, s.sede, c.capacidad, ds.salon FROM salones ds
            JOIN sedes s ON ds.id_sede = s.id_sede JOIN capacidades c ON ds.id_capacidad = c.id_capacidad;""")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id_salon': data[0],
                    'sede': data[1],
                    'capacidad':data[2],
                    'salon':data[3]
                   
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="salones not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_salonesid(self,id_salon:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT ds.id_salon, s.sede, c.capacidad, ds.salon FROM salones ds
            JOIN sedes s ON ds.id_sede = s.id_sede JOIN capacidades c ON ds.id_capacidad = c.id_capacidad where id_salon=%s
""", (id_salon,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                    'id_salon': result[0],
                    'sede': result[1],
                    'capacidad':result[2],
                    'salon':result[3]
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

    def create_salones(self, salones: Salones):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """select s.id_sede,c.id_capacidad from sedes s 
join capacidades c on c.capacidad=%s
where s.sede=%s""",(salones.capacidad,salones.sede,))
            result=cursor.fetchone()
            print(result)
            cursor.execute(
                "INSERT INTO salones (id_sede,id_capacidad,salon) VALUES (%s,%s,%s)", (result[0],result[1],salones.salon,))
            conn.commit()
            conn.close()
            return {"success": "salon creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "el salon ya ha sido creado"})
        finally:
            conn.close()
    def update_salon(self,data:Salones,id_salon):
        try:
           
            conn = get_db_connection()
            cursor = conn.cursor()
            print(data)
            cursor.execute("""select se.id_sede,c.id_capacidad from salones s
            join capacidades c on c.capacidad=%s
            join sedes se on se.sede=%s
            where s.id_salon=%s                              
                           
                           """,(data.capacidad,data.sede,id_salon))
            result=cursor.fetchone()
            print(result)
            cursor.execute("""update salones  set id_capacidad=%s,
                           id_sede=%s,salon=%s
                            where id_salon=%s""",(result[1],result[0],data.salon,id_salon))
            conn.commit()
            conn.close()
            return {"success":"el salon  ha sido actualizada"}
            

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return {"error":"el salon  se encuentra registrada en el programa"}
        finally:
            conn.close()
    
