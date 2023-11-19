import datetime
from typing import Any
import mysql.connector
from fastapi import HTTPException, UploadFile
from config.db_config import get_db_connection
from schemas.Horario import Horario
from fastapi.encoders import jsonable_encoder
from models.docente import ModelDocente
from models.user import ModelUser

success="el horario ha sido creado"


class HorarioController:
    def getHorario(self,id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
              SELECT ht.id_tutoria,f.facultad,p.programa,m.materia ,s.salon,ht.id_usuario,txe.estado,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final,se.sede  FROM `horario_tutorias` ht 
join salones s on ht.id_salon=s.id_salon
join tipoxestado txe on ht.id_estado_tutoria=txe.id_tipoxestado 
join fpxmateria fpxm on fpxm.id_fpxm=ht.id_fpxm
join facultadxprograma fxp on fxp.id_fxp=fpxm.id_fxp
join facultades f on f.id_facultad=fxp.id_facultad
join programas p on p.id_programa=fxp.id_programa
join materias m on m.id_materia=fpxm.id_materia
join sedes se on se.id_sede=s.id_sede
where  ht.id_tutoria=%s
""",(id,))
           
            data = cursor.fetchone()
            if data:
                payload = []
                content = {}

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
                       'sede':data[12]
                }
                

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="horario not found")

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def getHorarios(self):
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
where txe.id_tipoxestado=6 and ht.cupos>0
""")
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
                       'estado_tutoria':data[6],'cupos':data[7],
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
                    status_code=404, detail="facultadxprograma not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        
    def createHorario(self,horario:Horario,id_usuario:int):
        try:

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
select fpxm.id_fpxm from fpxmateria fpxm join facultadxprograma fxp on fxp.id_fxp=fpxm.id_fxp 
where fpxm.id_materia=%s and fxp.id_facultad=%s and fxp.id_programa=%s


""",(horario.id_materia,horario.id_facultad,horario.id_programa))
            id_fpxm=cursor.fetchone()[0]
            existTutoria=ModelDocente.verify_hour(horario.hora_inicial,horario.hora_final,horario.fecha,id_usuario)
            if(existTutoria==0):

                ModelDocente.createHorario( horario,id_usuario,id_fpxm)
                return {"success":success}
            else:
                return {"error":"el horario ya existe"}
           
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "el horario ya existe en el programa"})
        finally:
            conn.close()
            



    def updateHorario(self,horario:Horario,id:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            


            cursor.execute("""
UPDATE horario_tutorias 
SET cupos = %s, 
    tema = %s, 
    hora_inicial = %s, 
    hora_final = %s, 
    fecha = %s 
WHERE id_tutoria = %s
""", (horario.cupos, horario.tema, horario.hora_inicial, horario.hora_final, horario.fecha, id))
            

            
            conn.commit()
            conn.close()




            return {"resultado": "Horario  actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            print(err)
        finally:
            conn.close()
            
            
            
            




    def deleteHorario(self,id:int,id_user:int):
            try:
                fecha_actual=datetime.datetime.now()
                fecha_sin_microsegundos=fecha_actual.replace(microsecond=0)

                fecha_formateada = fecha_sin_microsegundos.strftime("%Y-%m-%d %H:%M:%S")
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("update horario_tutorias ht set ht.id_estado_tutoria=%s  where id_tutoria=%s",(8,id,))
                conn.commit()
                cursor.execute('INSERT INTO `registro_actividad`( `id_tipo_actividad`, `id_usuario`, `fecha_hora`, `ubicacion_actividad`) VALUES (%s,%s,%s,%s) ',(2,id_user,fecha_formateada,'eliminar tutoria'))
                conn.commit()
                conn.close()
                return {"success":"horario deshabilitado"}
            except mysql.connector.Error as err:
                print(err)
                conn.rollback()
            finally:
                conn.close()
    def deleteHorarioAdmin(self,id:int,id_user:int):
            try:
                fecha_actual=datetime.datetime.now()
                fecha_sin_microsegundos=fecha_actual.replace(microsecond=0)

                fecha_formateada = fecha_sin_microsegundos.strftime("%Y-%m-%d %H:%M:%S")
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("update horario_tutorias ht set ht.id_estado_tutoria=%s  where id_tutoria=%s",(8,id,))
                conn.commit()
                cursor.execute('INSERT INTO `registro_actividad`( `id_tipo_actividad`, `id_usuario`, `fecha_hora`, `ubicacion_actividad`) VALUES (%s,%s,%s,%s) ',(2,id_user,fecha_formateada,'eliminar tutoria'))
                conn.commit()
                conn.close()
                return {"success":"horario deshabilitado"}
            except mysql.connector.Error as err:
                print(err)
                conn.rollback()
            finally:
                conn.close()
    def getHorarioForIdUsuario(self,id:int):
        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            cursor.execute("""     SELECT ht.id_tutoria,f.facultad,p.programa,m.materia ,s.salon,ht.id_usuario,txe.estado,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final  FROM `horario_tutorias` ht 
join salones s on ht.id_salon=s.id_salon
join tipoxestado txe on ht.id_estado_tutoria=txe.id_tipoxestado 
join fpxmateria fpxm on fpxm.id_fpxm=ht.id_fpxm
join facultadxprograma fxp on fxp.id_fxp=fpxm.id_fxp
join facultades f on f.id_facultad=fxp.id_facultad
join programas p on p.id_programa=fxp.id_programa
join materias m on m.id_materia=fpxm.id_materia
where txe.id_tipoxestado=6 and id_usuario=%s;""",(id,))
            data=cursor.fetchall()
            payload=[]
            content={}
            for result in data:
                   content = {
                       'id':result[0],
                       'facultad':result[1],
                       'programa':result[2],
                       'materia':result[3],
                       'salon':result[4],
                       'id_usuario':result[5],
                       'estado_tutoria':result[6],
                       'cupos':result[7],
                       'tema':result[8],
                       'fecha':result[9],
                       'hora_inicial':result[10],
                       'hora_final':result[11]
                    

                }
                   payload.append(content)
                   
                   content={}
            json_data=jsonable_encoder(payload)
            print(json_data)
            if json_data:
                return {"resultado":json_data} 
            return {"error":"no existe ningun horario creado"}

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close() 
    async def createObservacion(self,file:UploadFile,id_user:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            resultados = []


            if file.filename.endswith(".txt"):
                contenido=await file.read()
            # Procesar archivos TXT
                texto = contenido.decode("utf-8")
                resultados.append(f"Contenido del archivo TXT {file.filename}: {texto}")
                
                return {"resultado": resultados[0]}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "el horario ya existe en el programa"})
        finally:
            conn.close()
    def agendarTutoria(self,id_tutoria:int,user_id:int):
        try:
            if(ModelUser.verificar_agendamiento(id_tutoria,user_id)==0):
              rpta=ModelUser.agendar_tutoria(id_tutoria,user_id)
              ModelUser.actualizarCupos(id_tutoria)
              return rpta
            return {"error":"la tutoria ya ha sido agendada"}
        except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)
    def obtenerTutoriasPendientes(self,id_user:int):
        try:
          rpta=ModelUser.obtenerTutoriasPendientes(id_user)
          return rpta
        except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)
    def cancelarTutoria(self,id_user,id_tutoria:int):
        try:
          rpta=ModelUser.cancelarTutoria(id_user,id_tutoria)
          ModelUser.recuperarCupos(id_tutoria)
          return rpta
        except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)
    def obtenerTutoriaFinalizada(self,id_user):
        try:
          rpta=ModelUser.obtenerTutoriaFinalizada(id_user)
          return rpta
        except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)
    def obtenerTutoriaFinalizadaDocente(self,id_user):
        try:
          rpta=ModelUser.obtenerTutoriaFinalizadaDocente(id_user)
          return rpta
        except Exception as e: 
            print(e)
            raise HTTPException(status_code=400, detail=e)
    
    def obtenerTutoriaFinalizadass(self):
        try:
          rpta=ModelUser.obtenerTutoriaFinalizadass()
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
