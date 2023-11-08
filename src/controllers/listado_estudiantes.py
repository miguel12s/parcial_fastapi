from typing import List
import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.listado import ModelListado
from schemas.ListadoEstudiante import ListadoEstudiante
from fastapi.encoders import jsonable_encoder

class ListadoController:
    def getListado(self,id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
               SELECT ht.id_tutoria,ht.id_usuario,concat(u.nombres," ",u.apellidos) as nombre_estudiante, le.id_usuario,txe.estado,m.materia,u.numero_documento,p.programa,le.asistencia,le.comentario  FROM `horario_tutorias` ht 
            join lista_estudiantes le on le.id_tutoria=ht.id_tutoria
            join salones s on ht.id_salon=s.id_salon
            join tipoxestado txe on ht.id_estado_tutoria=txe.id_tipoxestado 
            join fpxmateria fpxm on fpxm.id_fpxm=ht.id_fpxm
            join facultadxprograma fxp on fxp.id_fxp=fpxm.id_fxp
            join facultades f on f.id_facultad=fxp.id_facultad
            join programas p on p.id_programa=fxp.id_programa
            join materias m on m.id_materia=fpxm.id_materia
            join usuarios u on u.id_usuario=le.id_usuario
            where ht.id_tutoria=%s and txe.id_tipoxestado=6
 
""", (id,))
            data = cursor.fetchall()
            payload = []
            content = {}
            for i in data:
        

                content = {
                     'id_tutoria':i[0],
                       'id_docente':i[1],
                       'nombre_estudiante':i[2],
                       'id_estudiante':i[3],
                       'estado_tutoria':i[4],
                       'materia':i[5],
                       'numero_documento':i[6],
                       'programa':i[7],
                       'asistencia':i[8],
                       'comentario':i[9]
                }
                payload.append(content)
                content={}
            json_data = jsonable_encoder(payload)
            if data:
                return {"resultado":json_data}
            else:
                return {"error":"no existen estudiantes en el listado "}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def getListados(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
SELECT * FROM `lista_estudiantes` WHERE 1
""")
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'id_horario': data[1],
                    'id_usuario':data[2],
                    'comentario':data[3],
                    'asistencia':str(data[4]),
                   

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="listado de estudiante not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        
    def createListado(self,listado:ListadoEstudiante):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            asistencia:int= 1 if listado.asistencia=="asistio"  else 0
            print(asistencia)
            cursor.execute(
                "INSERT INTO lista_estudiantes (id_tutoria,id_usuario,comentario,asistencia) VALUES (%s,%s,%s,%s)", (listado.id_horario,listado.id_usuario,listado.comentario,asistencia,))
            conn.commit()
            conn.close()
            return {"resultado": "lista de estudiantes  creada"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "la lista de estudiantes  ya existe en el programa"})
        finally:
            conn.close()     



    def updateListado(self,listado:ListadoEstudiante,id:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            

            print(id)
            cursor.execute("""
UPDATE lista_estudiantes
SET comentario=%s,asistencia=%s
WHERE id_lista = %s
""", (listado.comentario,listado.asistencia,id,))
            

            
            conn.commit()
            conn.close()




            return {"resultado": "lista  actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            print(err)
        finally:
            conn.close()
    def deleteListado(self,id:int):
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("delete from lista_estudiantes where id_lista=%s",(id,))
                conn.commit()
                conn.close()
                return {"success":"lista de estudiantes eliminado"}
            except mysql.connector.Error as err:
                print(err)
                conn.rollback()
            finally:
                conn.close()
            pass
    def pasarLista(self,id_user:int,listado:List[ListadoEstudiante]):
        try:
          rpta=ModelListado.pasarLista(id_user,listado)
          ModelListado.actualizarEstadoTutoria(id_user,listado)
          return rpta
        except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)
    # def createHorario(self,horario:Horario):
    #     try:
    #         conn = get_db_connection()
    #         cursor = conn.cursor()
    #         cursor.execute(
    #             """SELECT id_tipo_actividad FROM tipo_registro_actividad WHERE tipo_registro_actividad.tipo_actividad=%s""",(registroactividad.tipo_actividad,))
            
    #         result=cursor.fetchone()
    #         cursor.execute("""insert into registro_actividad ( id_tipo_actividad,id_usuario,fecha,hora,ubicacion_actividad) values
    #         (%s,%s,%s,%s,%s)""",(result[0],registroactividad.id_usuario,registroactividad.fecha,registroactividad.hora,registroactividad.ubicacion_actividad,))
    #         conn.commit()
    #         conn.close()
    #         return {"resultado": "registro actividad  creado"}
    #     except mysql.connector.Error as err:
    #         print(err)
    #         conn.rollback()
    #         return ({"error": "registro actividad ya existe en el programa"})
    #     finally:
    #         conn.close()
    #     pass
