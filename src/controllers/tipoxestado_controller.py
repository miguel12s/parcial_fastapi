
import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.TipoxEstado import TipoxEstado
from fastapi.encoders import jsonable_encoder


class TipoxEstadoController():
    def getTipoxEstados(self):
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
SELECT txe.id_tipoxestado,te.tipo_estado,txe.estado FROM tipoxestado txe join tipoestado te on txe.id_tipoestado=te.id_tipoestado 
""")
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'tipoxestado': data[1],
                    'estado':data[2]
                   

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="tipoxestado not found")

        

    def getTipoxEstado(self,id_tipoxestado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT txe.id_tipoxestado,te.tipo_estado,txe.estado FROM tipoxestado txe join tipoestado te on txe.id_tipoestado=te.id_tipoestado  where txe.id_tipoxestado=%s
""", (id_tipoxestado,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                      'id': result[0],
                    'tipoxestado': result[1],
                    'estado':result[2]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="tipoxestado not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()



    def createTipoxEstado(self, tipoxestado: TipoxEstado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id_tipoestado FROM tipoestado WHERE tipo_estado=%s", (tipoxestado.tipoxestado,))
            result = cursor.fetchone()
            print(result)
            cursor.execute(
                "INSERT INTO tipoxestado (id_tipoestado,estado) VALUES (%s,%s)", 
                (result[0],tipoxestado.estado,))
            conn.commit()
            conn.close()
            return {"success": "tipoxestado creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "tipoxestado  ya existe en el programa"})
        finally:
            conn.close()

    def updateTipoxEstado(self, tipoxestado: TipoxEstado,id:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            print(tipoxestado)
            cursor.execute("select id_tipoestado from tipoestado where tipo_estado=%s",(tipoxestado.tipoxestado,))
            result=cursor.fetchone()
            print(result)
            cursor.execute("update tipoxestado set id_tipoestado=%s ,estado=%s where id_tipoxestado=%s ",(result[0],tipoxestado.estado,id))
            conn.commit()
            conn.close()
            return {"success": "tipoxestado creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "tipoxestado  ya existe en el programa"})
        finally:
            conn.close()
    def getTipoxEstadosForUser(self):
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
SELECT txe.id_tipoxestado,te.tipo_estado,txe.estado FROM tipoxestado txe join tipoestado te on txe.id_tipoestado=te.id_tipoestado  where txe.id_tipoestado=4
""")
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'tipoxestado': data[1],
                    'estado':data[2]
                   

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="tipoxestado not found")