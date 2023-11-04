import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from schemas.CampoxUsuario import CampoxUsuario
from fastapi.encoders import jsonable_encoder

class CampoxUsuarioController:
    def getCampoxUsuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT cxu.id_campoxusu,cxu.id_usuario, ca.campo,cxu.dato campo FROM `camposxusuario` cxu join campoad ca on cxu.id_campo=ca.id_campo ")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id':data[0],
        'id_usuario':data[1],
    'campo':data[2],
    'dato': data[3]

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
        

    def getCampoxUsuario(self,id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT cxu.id_campoxusu,cxu.id_usuario, ca.campo,cxu.dato campo FROM `camposxusuario` cxu join campoad ca on cxu.id_campo=ca.id_campo where id_campoxusu=%s""", (id,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                        'id':result[0],
        'id_usuario':result[1],
    'campo':result[2],
    'dato': result[3]
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



    def createCampoxUsuario(self,campoxusuario:CampoxUsuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT campoad.id_campo from campoad where campoad.campo=%s""",(campoxusuario.campo,))
            
            result=cursor.fetchone()
            cursor.execute("""insert into camposxusuario ( id_usuario, id_campo, dato) values
            (%s,%s,%s)""",(campoxusuario.id_usuario,result[0],campoxusuario.dato,))
            conn.commit()
            conn.close()
            return {"resultado": "campoxusuario  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "campoxusuario  ya existe en el programa"})
        finally:
            conn.close()
        pass
