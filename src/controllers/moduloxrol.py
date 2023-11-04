import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.ModuloxRol import Moduloxrol
from fastapi.encoders import jsonable_encoder

class ModuloxRolController():
    def createModuloxRol(self,moduloxrol:Moduloxrol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT id_materia,txe.id_tipoxestado from materias join tipoxestado  txe on txe.estado=%s  where materias.materia=%s""",(moduloxrol.estado,moduloxrol.materia,))
            
            result=cursor.fetchone()
            cursor.execute("""insert into moduloxrol ( id_materia,id_usuario,id_estado) values
            (%s,%s,%s)""",(result[0],moduloxrol.id_usuario,result[1],))
            conn.commit()
            conn.close()
            return {"resultado": "moduloxrol creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "moduloxrol ya existe en el programa"})
        finally:
            conn.close()


    def getModulosxRol(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT mxr.id_mxr,m.materia,mxr.id_usuario,te.estado FROM moduloxrol mxr join materias m  on mxr.id_materia=m.id_materia join tipoxestado te on mxr.id_estado=te.id_tipoxestado")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id':int(data[0]),
        'materia':data[1],
    'id_usuario':int(data[2]),
    'estado': (data[3])

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="moduloxrol not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def getModuloxRol(self,id:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
SELECT mxr.id_mxr,m.materia,mxr.id_usuario,te.estado FROM moduloxrol mxr join materias m  on mxr.id_materia=m.id_materia join tipoxestado te on mxr.id_estado=te.id_tipoxestado where id_mxr=%s

""",(id,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                           'id':int(result[0]),
        'materia':result[1],
    'id_usuario':int(result[2]),
    'estado': (result[3]) 
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="moduloxrol not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()