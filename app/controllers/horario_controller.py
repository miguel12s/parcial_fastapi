from typing import Any
import mysql.connector
from fastapi import HTTPException, UploadFile
from config.db_config import get_db_connection
from models.Horario import Horario
from fastapi.encoders import jsonable_encoder
class HorarioController:
    def getHorario(self,id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            sql="""
               SELECT ht.id_tutoria,f.facultad,p.programa,s.salon,ht.id_usuario,txe.estado,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final  FROM `horario_tutorias` ht join salones s on ht.id_salon=s.id_salon join tipoxestado txe on ht.id_estado_tutoria=txe.id_tipoxestado join facultadxprograma fxp on ht.id_fxp=fxp.id_fxp join facultades f on fxp.id_facultad=f.id_facultad join programas p on fxp.id_programa=p.id_programa where id_usuario=%s
"""
            cursor.execute(sql, (id,))
            print(sql)
            data = cursor.fetchone()
            if data:
                payload = []
                content = {}

                content = {
                   'id':data[0],
                       'facultad':data[1],
                       'programa':data[2],
                       'salon':data[3],
                       'id_usuario':data[4],
                       'estado_tutoria':data[5],
                       'cupos':data[6],
                       'tema':data[7],
                       'fecha':data[8],
                       'hora_inicial':data[9],
                       'hora_final':data[10]
                }
                payload.append(content)

                json_data = jsonable_encoder(payload)
                print(json_data)
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
SELECT ht.id_tutoria,f.facultad,p.programa,ma.materia,s.salon,ht.id_usuario,txe.estado,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final  FROM `horario_tutorias` ht join salones s on ht.id_salon=s.id_salon join tipoxestado txe on ht.id_estado_tutoria=txe.id_tipoxestado join facultadxprograma fxp on ht.id_fxp=fxp.id_fxp join facultades f on fxp.id_facultad=f.id_facultad join programas p on fxp.id_programa=p.id_programa join moduloxrol mxr on ht.id_mxr=mxr.id_mxr join materias ma on mxr.id_materia=ma.id_materia
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
                       'hora_final':data[11]
                    

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
        
    def createHorario(self,horario:Horario):
        try:
            print(horario)
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
select fpxm.id_fpxm from facultadxprograma fxp where fxp.id_facultad=%s
and fxp.id_programa=%s 

""",(horario.id_facultad,horario.id_programa))
            id_fxp=cursor.fetchone()[0]
            cursor.execute("""
select mxr.id_mxr,txe.id_tipoestado,s.id_salon from moduloxrol mxr join tipoxestado txe on txe.estado=%s join salones s on s.salon=%s  where mxr.id_materia=(select m.id_materia from  materias m where m.materia=%s and mxr.id_tutoria=%s)
""",(horario.estado_tutoria,horario.salon,horario.materia,horario.id_usuario,))
            result=cursor.fetchone()
          
            cursor.execute("""
    INSERT INTO horario_tutorias (id_fxp, id_mxr, id_salon, id_usuario, id_estado_tutoria, cupos, tema, fecha, hora_inicial, hora_final)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s, %s, %s)

""",(id_fxp,result[0],result[2],horario.id_usuario,result[1],horario.cupos,horario.tema,horario.fecha,horario.hora_inicial,horario.hora_final))
            conn.commit()
            conn.close()
            return {"resultado": "horario creado"}
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
            
            
            
            




    def deleteHorario(self,id:int):
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("delete from horario_tutorias where id_tutoria=%s",(id,))
                conn.commit()
                conn.close()
                return {"success":"horario eliminado"}
            except mysql.connector.Error as err:
                print(err)
                conn.rollback()
            finally:
                conn.close()
    def getHorarioForIdUsuario(self,id:int):
        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            cursor.execute("""       SELECT ht.id_tutoria,f.facultad,p.programa,s.salon,ht.id_usuario,txe.estado,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final  FROM `horario_tutorias` ht join salones s on ht.id_salon=s.id_salon join tipoxestado txe on ht.id_estado_tutoria=txe.id_tipoxestado join facultadxprograma fxp on ht.id_fxp=fxp.id_fxp join facultades f on fxp.id_facultad=f.id_facultad join programas p on fxp.id_programa=p.id_programa where id_usuario=%s""",(id,))
            data=cursor.fetchall()
            payload=[]
            content={}
            for result in data:
                   content = {
                       'id':result[0],
                       'facultad':result[1],
                       'programa':result[2],
                       'salon':result[3],
                       'id_usuario':result[4],
                       'estado_tutoria':result[5],'cupos':result[6],
                       'tema':result[7],
                       'fecha':result[8],
                       'hora_inicial':result[9],
                       'hora_final':result[10]
                    

                }
                   payload.append(content)
                   
                   content={}
            json_data=jsonable_encoder(payload)
            print(json_data)
            if json_data:
                return {"resultado":json_data}
            return {"error":"no existe ningun horario creado"}

        except mysql.connector.Error as err:
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
