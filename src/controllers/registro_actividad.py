import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.RegistroActividad import RegistroActividad
from fastapi.encoders import jsonable_encoder

class RegistroActividadController:
    def getRegistroActividad(self,id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT ra.id_registro_actividad,tra.tipo_actividad,ra.id_usuario,ra.fecha,ra.hora,ra.ubicacion_actividad FROM registro_actividad ra join tipo_registro_actividad tra on tra.id_tipo_actividad=ra.id_tipo_actividad where ra.id_registro_actividad=%s
""", (id,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                   'id': result[0],
                    'tipo_actividad': result[1],
                    'id_usuario':result[2],
                    'fecha':result[3],
                    'hora':result[4],
                    'ubicacion_actividad':result[5]
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
    def getRegistrosActividad(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
SELECT 
ra.id_registro_actividad
,tra.tipo_actividad
,concat(u.nombres,' ',u.apellidos) as nombre_completo
,ra.fecha_hora
,ra.ubicacion_actividad
FROM registro_actividad ra 
join tipo_registro_actividad tra on tra.id_tipo_actividad=ra.id_tipo_actividad 
join usuarios u on u.id_usuario=ra.id_usuario
""")
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'tipo_actividad': data[1],
                    'nombre_completo':data[2],
                    'fecha_hora':data[3],
                    'ubicacion':data[4]
                   

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="facultadxprograma not found")

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def createRegistroActividad(self,registroactividad:RegistroActividad):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT id_tipo_actividad FROM tipo_registro_actividad WHERE tipo_registro_actividad.tipo_actividad=%s""",(registroactividad.tipo_actividad,))
            
            result=cursor.fetchone()
            cursor.execute("""insert into registro_actividad ( id_tipo_actividad,id_usuario,fecha,hora,ubicacion_actividad) values
            (%s,%s,%s,%s,%s)""",(result[0],registroactividad.id_usuario,registroactividad.fecha,registroactividad.hora,registroactividad.ubicacion_actividad,))
            conn.commit()
            conn.close()
            return {"resultado": "registro actividad  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "registro actividad ya existe en el programa"})
        finally:
            conn.close()
        pass
