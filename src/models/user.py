from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from utils.utils import Hasher
from schemas.Materia import Materia
from config.db_config import get_db_connection
import mysql.connector

class ModelUser:
    def verificar_agendamiento(id_tutoria:int,id_usuario:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            sql="select count(*) from lista_estudiantes where id_usuario=%s and id_tutoria=%s"
            cursor.execute(sql,(id_usuario,id_tutoria))
            print(sql)
            tutoria_agendada=cursor.fetchone()[0]
            print(tutoria_agendada)
            return tutoria_agendada
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "el horario ya existe en el programa"})
        finally:
            conn.close()
    def agendar_tutoria(id_tutoria:int,id_usuario:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            sql="insert into lista_estudiantes (id_tutoria,id_usuario) values (%s,%s)"
            cursor.execute(sql,(id_tutoria,id_usuario,))
            conn.commit()
            conn.close()
            return {"message":"la tutoria ha sido agendada con exito"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def actualizarCupos(id_tutoria):
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            sql="update horario_tutorias set cupos=cupos-1  where id_tutoria=%s"
            cursor.execute(sql,(id_tutoria,))
            
            conn.commit()
            conn.close()
         except mysql.connector.Error as err:
            print(err)
            conn.rollback()
         finally:
            conn.close()
    def obtenerTutoriasPendientes(user_id:int):
     try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
SELECT ht.id_tutoria,f.facultad,p.programa,m.materia ,s.salon,le.id_usuario,txe.estado,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final,u.nombres,u.apellidos  FROM `horario_tutorias` ht 
join lista_estudiantes le on le.id_tutoria=ht.id_tutoria
join salones s on ht.id_salon=s.id_salon
join tipoxestado txe on ht.id_estado_tutoria=txe.id_tipoxestado 
join fpxmateria fpxm on fpxm.id_fpxm=ht.id_fpxm
join facultadxprograma fxp on fxp.id_fxp=fpxm.id_fxp
join facultades f on f.id_facultad=fxp.id_facultad
join programas p on p.id_programa=fxp.id_programa
join materias m on m.id_materia=fpxm.id_materia
join usuarios u on u.id_usuario=ht.id_usuario
where txe.id_tipoxestado=6 and le.id_usuario=%s
""",(user_id,))
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                content = {
                       'id':data[0],
                       'facultad':data[1],
                       'programa':data[2],
                       'materia':data[3],
                       'salon':data[4],
                       'id_usuario':data[5],
                       'estado_tutoria':data[6],
                       'cupos':data[7],
                       'tema':data[8],
                       'fecha':data[9],
                       'hora_inicial':data[10],
                       'hora_final':data[11],
                       'nombres':data[12],
                       'apellidos':data[13]
                    

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="tutorias no encontradas")
     
     except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)
    def cancelarTutoria(id_user,id_tutoria):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            sql="delete  from lista_estudiantes where id_tutoria=%s and id_usuario=%s"
            cursor.execute(sql,(id_tutoria,id_user))
            
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def recuperarCupos(id_tutoria):
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            sql="update horario_tutorias set cupos=cupos+1  where id_tutoria=%s"
            cursor.execute(sql,(id_tutoria,))
            
            conn.commit()
            conn.close()
         except mysql.connector.Error as err:
            print(err)
            conn.rollback()
         finally:
            conn.close()
    def obtenerTutoriaFinalizada(user_id:int):
     try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            SELECT ht.id_tutoria,f.facultad,p.programa,m.materia ,s.salon,le.id_usuario,txe.estado,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final,u.nombres,u.apellidos,le.comentario  FROM `horario_tutorias` ht 
            join lista_estudiantes le on le.id_tutoria=ht.id_tutoria
            join salones s on ht.id_salon=s.id_salon
            join tipoxestado txe on ht.id_estado_tutoria=txe.id_tipoxestado 
            join fpxmateria fpxm on fpxm.id_fpxm=ht.id_fpxm
            join facultadxprograma fxp on fxp.id_fxp=fpxm.id_fxp
            join facultades f on f.id_facultad=fxp.id_facultad
            join programas p on p.id_programa=fxp.id_programa
            join materias m on m.id_materia=fpxm.id_materia
            join usuarios u on u.id_usuario=ht.id_usuario
            where txe.id_tipoxestado=2 and le.id_usuario=%s
            """,(user_id,))
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                content = {
                       'id':data[0],
                       'facultad':data[1],
                       'programa':data[2],
                       'materia':data[3],
                       'salon':data[4],
                       'id_usuario':data[5],
                       'estado_tutoria':data[6],
                       'cupos':data[7],
                       'tema':data[8],
                       'fecha':data[9],
                       'hora_inicial':data[10],
                       'hora_final':data[11],
                       'nombres':data[12],
                       'apellidos':data[13],
                       'observacion':data[14]
                    

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
               return {"error":"no hay tutorias finalizadas"}
     
     except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)
    def obtenerTutoriaFinalizadaDocente(user_id:int):
     try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
             SELECT ht.id_tutoria,f.facultad,p.programa,m.materia ,s.salon,ht.id_usuario,txe.estado,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final,u.nombres,u.apellidos  FROM `horario_tutorias` ht 
            join salones s on ht.id_salon=s.id_salon
            join tipoxestado txe on ht.id_estado_tutoria=txe.id_tipoxestado 
            join fpxmateria fpxm on fpxm.id_fpxm=ht.id_fpxm
            join facultadxprograma fxp on fxp.id_fxp=fpxm.id_fxp
            join facultades f on f.id_facultad=fxp.id_facultad
            join programas p on p.id_programa=fxp.id_programa
            join materias m on m.id_materia=fpxm.id_materia
            join usuarios u on u.id_usuario=ht.id_usuario
            where txe.id_tipoxestado=2 and ht.id_usuario=%s
            """,(user_id,))
            print(user_id)
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                print(content)
                content = {
                       'id':data[0],
                       'facultad':data[1],
                       'programa':data[2],
                       'materia':data[3],
                       'salon':data[4],
                       'id_usuario':data[5],
                       'estado_tutoria':data[6],
                       'cupos':data[7],
                       'tema':data[8],
                       'fecha':data[9],
                       'hora_inicial':data[10],
                       'hora_final':data[11],
                       'nombres':data[12],
                       'apellidos':data[13]
                    

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
               return {"error":"no hay tutorias finalizadas"}
     
     except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)
    



    def obtenerTutoriaFinalizadass():
     try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
             SELECT ht.id_tutoria,f.facultad,p.programa,m.materia ,s.salon,ht.id_usuario,txe.estado,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final,u.nombres,u.apellidos  FROM `horario_tutorias` ht 
            join salones s on ht.id_salon=s.id_salon
            join tipoxestado txe on ht.id_estado_tutoria=txe.id_tipoxestado 
            join fpxmateria fpxm on fpxm.id_fpxm=ht.id_fpxm
            join facultadxprograma fxp on fxp.id_fxp=fpxm.id_fxp
            join facultades f on f.id_facultad=fxp.id_facultad
            join programas p on p.id_programa=fxp.id_programa
            join materias m on m.id_materia=fpxm.id_materia
            join usuarios u on u.id_usuario=ht.id_usuario
            where txe.id_tipoxestado=2 
            """)
            
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {}
            for data in result:
                print(content)
                content = {
                       'id':data[0],
                       'facultad':data[1],
                       'programa':data[2],
                       'materia':data[3],
                       'salon':data[4],
                       'id_usuario':data[5],
                       'estado_tutoria':data[6],
                       'cupos':data[7],
                       'tema':data[8],
                       'fecha':data[9],
                       'hora_inicial':data[10],
                       'hora_final':data[11],
                       'nombres':data[12],
                       'apellidos':data[13]
                    

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
               return {"error":"no hay tutorias finalizadas"}
     
     except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)