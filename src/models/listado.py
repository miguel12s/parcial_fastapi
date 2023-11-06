from typing import List
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from schemas.ListadoEstudiante import ListadoEstudiante
from schemas.changePassword import ChangePassword
from utils.utils import Hasher
from schemas.Materia import Materia
from config.db_config import get_db_connection
import mysql.connector

class ModelListado:
        

    def pasarLista(id_user: int,listado:List[ListadoEstudiante]):
        try:
            observacion=0
            conn = get_db_connection()
            cursor = conn.cursor()
            for data in listado :
                print(data)
                temp=observacion if data.asistencia==False else 1
                print(temp)
                sql="update lista_estudiantes set comentario=%s,asistencia=%s where id_tutoria=%s and id_usuario=%s"
                cursor.execute(sql,(data.observacion,temp,data.id_tutoria,data.id_usuario))

                conn.commit()

            
            return {"success":"el listado de estudiantes ha sido modificado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def actualizarEstadoTutoria(id_user: int,listado:List[ListadoEstudiante]):
        try:
            observacion=0
            conn = get_db_connection()
            cursor = conn.cursor()
            for data in listado :
                id_tutoria=data.id_tutoria
            sql="update horario_tutorias set id_estado_tutoria=%s where id_tutoria=%s and id_usuario=%s"
            cursor.execute(sql,(2,id_tutoria,id_user))

            conn.commit()

            
            return {"success":"el listado de estudiantes ha sido modificado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    

    