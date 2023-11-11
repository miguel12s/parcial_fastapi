
import tempfile
from fastapi import HTTPException
from fastapi.responses import FileResponse
from config.db_config import get_db_connection
import mysql.connector
import pandas as pd
import datetime
from schemas.Range import Range
class ModelReport():

    def obtenerListadoEstudiantes(data:Range):
        try:
            if data.type_report=="usuarios":
                file=ModelReport.generar_informe_usuarios(data.start_date,data.end_date)
                return file
            elif data.type_report=="tutorias eliminadas":
                file=ModelReport.generar_informe_tutorias_eliminadas(data.start_date,data.end_date)
                return file
            elif data.type_report=="tutorias creadas":
                file=ModelReport.generar_informe_tutorias_creadas(data.start_date,data.end_date)
                return file
            elif data.type_report=="tutorias finalizadas":
                file=ModelReport.generar_informe_tutorias_finalizadas(data.start_date,data.end_date)
                return file
            elif data.type_report=="usuarios deshabilitados":
                file=ModelReport.generar_informe_usuarios_deshabilitados(data.start_date,data.end_date)
                return file
            
        except Exception as e:
            raise HTTPException(status_code=500,detail="error en el servidor")
        
    def generar_informe_usuarios(fecha_inicio:str, fecha_final:str):
     try:
        conn = get_db_connection()
        cursor = conn.cursor()
        print(fecha_inicio, fecha_final)

        # Convierte las fechas al formato 'yyyy-mm-dd' para la consulta a la API
        fecha_inicio_api = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_final_api = datetime.datetime.strptime(fecha_final, '%Y-%m-%d')
        # Realiza el ajuste de un día si es mayor y de un día si es menor
        fecha_inicio_api -= datetime.timedelta(days=1)
        fecha_final_api += datetime.timedelta(days=1)

        fecha_inicio_api = fecha_inicio_api.strftime('%Y-%m-%d')  # La fecha de inicio ajustada
        fecha_final_api = fecha_final_api.strftime('%Y-%m-%d')

        
        print(fecha_inicio_api, fecha_final_api)

        cursor.execute("""
            SELECT u.id_usuario, u.nombres, u.apellidos, u.numero_documento, td.tipo_documento, ra.fecha_hora, f.facultad, p.programa, u.celular, u.correo
            FROM registro_actividad ra
            JOIN usuarios u ON u.id_usuario = ra.id_usuario
            JOIN tipos_documento td ON td.id_tipo_documento = u.id_tipo_documento
            JOIN fpxusuario facusu ON facusu.id_usuario = u.id_usuario
            JOIN facultadxprograma fxp ON fxp.id_fxp = facusu.id_fxp
            JOIN facultades f ON f.id_facultad = fxp.id_facultad
            JOIN programas p ON p.id_programa = fxp.id_programa
            WHERE ra.fecha_hora >= STR_TO_DATE(%s, '%Y-%m-%d')
            AND ra.fecha_hora <= STR_TO_DATE(%s, '%Y-%m-%d');
        """, (fecha_inicio_api, fecha_final_api))

        result = cursor.fetchall()
        print(result)
        payload = []
        content = {}
        for data in result:
            fecha_valida = data[5].strftime('%d-%m-%Y')
            print(fecha_valida)
            content = {
                'codigo': data[0],
                'nombres': data[1],
                'apellido': data[2],
                'numero_documento': data[3],
                'tipo_documento': data[4],
                'fecha_creacion': fecha_valida,
                "facultad": data[6],
                "programa": data[7],
                "celular": data[8],
                "correo": data[9]
            }
            print(data[5])
            payload.append(content)
            content = {}

        df = pd.DataFrame(payload)
        # Generar un archivo temporal para el informe
         
        # Generar un archivo temporal para el informe
        with tempfile.NamedTemporaryFile(delete=True, suffix=".xlsx") as tmp_file:file_name = tmp_file.name
                # Guardar el DataFrame en el archivo temporal
        df.to_excel(file_name, sheet_name="hoja 1", index=False)
                # Devolver el archivo temporal como respuesta
        return FileResponse(file_name, filename="Reporte_horario.xlsx")
        

     except mysql.connector.Error as err:
        print(err)
        conn.rollback()
     finally:
        conn.close()









    def generar_informe_usuarios_deshabilitados(fecha_inicio,fecha_final):
        try:
                conn = get_db_connection()
                cursor = conn.cursor()

# Convierte las fechas al formato 'yyyy-mm-dd' para la consulta a la API
                fecha_inicio_api = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
                fecha_final_api = datetime.datetime.strptime(fecha_final, '%Y-%m-%d')
                # Realiza el ajuste de un día si es mayor y de un día si es menor
                fecha_inicio_api -= datetime.timedelta(days=1)
                fecha_final_api += datetime.timedelta(days=1)

                fecha_inicio_api = fecha_inicio_api.strftime('%Y-%m-%d')  # La fecha de inicio ajustada
                fecha_final_api = fecha_final_api.strftime('%Y-%m-%d')

                
                cursor.execute("""

    SELECT u.id_usuario, u.nombres,u.apellidos,u.numero_documento,td.tipo_documento,ra.fecha_hora,f.facultad,p.programa,u.celular,u.correo
    FROM registro_actividad ra
    JOIN usuarios u on u.id_usuario = ra.id_usuario
    join tipos_documento td on td.id_tipo_documento=u.id_tipo_documento
    join tipoxestado txe on txe.id_tipoxestado=u.id_estado
    join fpxusuario facusu on facusu.id_usuario=u.id_usuario     
    join facultadxprograma fxp on fxp.id_fxp=facusu.id_fxp
    join facultades f on f.id_facultad=fxp.id_facultad 
    join programas p on p.id_programa=fxp.id_programa
    WHERE ra.fecha_hora >=STR_TO_DATE(%s, '%Y-%m-%d')
    AND ra.fecha_hora <= STR_TO_DATE(%s, '%Y-%m-%d') and u.id_estado=14
    group by u.id_usuario;
    """,(fecha_inicio_api,fecha_final_api))
                result = cursor.fetchall()
                print(result)
                payload = []
                content = {}
                for data in result:
                    fecha_valida=data[5].strftime( '%d-%m-%Y')
                    print(fecha_valida)
                    content = {
                        'codigo': data[0],
                        'nombres': data[1],
                        'apellido':data[2],
                        'numero_documento':data[3],
                        'tipo_documento':data[4],
                        'fecha_creacion':fecha_valida,
                        "facultad":data[6],
                        "programa":data[7],
                        "celular":data[8],
                        "correo":data[9]

                    

                    }
                    print(data[5])
                    payload.append(content)
                    content = {}
                df = pd.DataFrame(payload)
                # Generar un archivo temporal para el informe
                with tempfile.NamedTemporaryFile(delete=True, suffix=".xlsx") as tmp_file:file_name = tmp_file.name
                # Guardar el DataFrame en el archivo temporal
                df.to_excel(file_name, sheet_name="hoja 1", index=False)
                # Devolver el archivo temporal como respuesta
                return FileResponse(file_name, filename="Usuarios_deshabilitados.xlsx")
            

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def generar_informe_tutorias_eliminadas(fecha_inicio,fecha_final):
       
         try:
                conn = get_db_connection()
                cursor = conn.cursor()

# Convierte las fechas al formato 'yyyy-mm-dd' para la consulta a la API
                fecha_inicio_api = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
                fecha_final_api = datetime.datetime.strptime(fecha_final, '%Y-%m-%d')
                # Realiza el ajuste de un día si es mayor y de un día si es menor
                fecha_inicio_api -= datetime.timedelta(days=1)
                fecha_final_api += datetime.timedelta(days=1)

                fecha_inicio_api = fecha_inicio_api.strftime('%Y-%m-%d')  # La fecha de inicio ajustada
                fecha_final_api = fecha_final_api.strftime('%Y-%m-%d')

                
                cursor.execute("""

  SELECT ht.id_tutoria,concat(u.nombres,' ',u.apellidos) as nombre_completo,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final,s.salon,se.sede,txe.estado
FROM `horario_tutorias` ht
inner join usuarios u on ht.id_usuario=u.id_usuario
inner join salones s on s.id_salon=ht.id_salon
inner join sedes se on se.id_sede=s.id_sede
inner join tipoxestado txe on txe.id_tipoxestado=ht.id_estado_tutoria
where ht.id_estado_tutoria=8 
and ht.fecha >= STR_TO_DATE(%s, '%Y-%m-%d')
 and ht.fecha <= STR_TO_DATE(%s, '%Y-%m-%d');
    """,(fecha_inicio_api,fecha_final_api))
                result = cursor.fetchall()
                print(result)
                payload = []
                content = {}
                for data in result:
                    fecha_valida=data[4].strftime( '%d-%m-%Y')
                    print(fecha_valida)
                    content = {
                        'codigo': data[0],
                        'nombre_completo':data[1],
                        'cupos':data[2],
                        'tema':data[3],
                        'fecha':fecha_valida,
                        'hora_inicial':data[5],
                        'hora_final':data[6],
                        'salon':data[7],
                        'sede':data[8],
                        'estado':data[9]
                    

                    

                    }
                    print(data[5])
                    payload.append(content)
                    content = {}
                df = pd.DataFrame(payload)
                # Generar un archivo temporal para el informe
                with tempfile.NamedTemporaryFile(delete=True, suffix=".xlsx") as tmp_file:file_name = tmp_file.name
                # Guardar el DataFrame en el archivo temporal
                df.to_excel(file_name, sheet_name="hoja 1", index=False)
                # Devolver el archivo temporal como respuesta
                return FileResponse(file_name, filename="Reporte_tutorias_eliminadas_horario.xlsx")
        
            

         except mysql.connector.Error as err:
            print(err)
            conn.rollback()
         finally:
            conn.close()

    def generar_informe_tutorias_creadas(fecha_inicio,fecha_final):
       
         try:
                conn = get_db_connection()
                cursor = conn.cursor()

# Convierte las fechas al formato 'yyyy-mm-dd' para la consulta a la API
                fecha_inicio_api = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
                fecha_final_api = datetime.datetime.strptime(fecha_final, '%Y-%m-%d')
                # Realiza el ajuste de un día si es mayor y de un día si es menor
                fecha_inicio_api -= datetime.timedelta(days=1)
                fecha_final_api += datetime.timedelta(days=1)

                fecha_inicio_api = fecha_inicio_api.strftime('%Y-%m-%d')  # La fecha de inicio ajustada
                fecha_final_api = fecha_final_api.strftime('%Y-%m-%d')

                
                cursor.execute("""

  SELECT ht.id_tutoria,concat(u.nombres,' ',u.apellidos) as nombre_completo,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final,s.salon,se.sede,txe.estado
FROM `horario_tutorias` ht
inner join usuarios u on ht.id_usuario=u.id_usuario
inner join salones s on s.id_salon=ht.id_salon
inner join sedes se on se.id_sede=s.id_sede
inner join tipoxestado txe on txe.id_tipoxestado=ht.id_estado_tutoria
where ht.id_estado_tutoria=6
and ht.fecha >= STR_TO_DATE(%s, '%Y-%m-%d')
 and ht.fecha <= STR_TO_DATE(%s, '%Y-%m-%d');
    """,(fecha_inicio_api,fecha_final_api))
                result = cursor.fetchall()
                print(result)
                payload = []
                content = {}
                for data in result:
                    fecha_valida=data[4].strftime( '%d-%m-%Y')
                    print(fecha_valida)
                    content = {
                        'codigo': data[0],
                        'nombre_completo':data[1],
                        'cupos':data[2],
                        'tema':data[3],
                        'fecha':fecha_valida,
                        'hora_inicial':data[5],
                        'hora_final':data[6],
                        'salon':data[7],
                        'sede':data[8],
                        'estado':data[9]
                    

                    

                    }
                    print(data[5])
                    payload.append(content)
                    content = {}
                df = pd.DataFrame(payload)
                # Generar un archivo temporal para el informe
                with tempfile.NamedTemporaryFile(delete=True, suffix=".xlsx") as tmp_file:file_name = tmp_file.name
                # Guardar el DataFrame en el archivo temporal
                df.to_excel(file_name, sheet_name="hoja 1", index=False)
                # Devolver el archivo temporal como respuesta
                return FileResponse(file_name, filename="Reporte_tutorias_creadas.xlsx")
        
            

         except mysql.connector.Error as err:
            print(err)
            conn.rollback()
         finally:
            conn.close()
    def generar_informe_tutorias_finalizadas(fecha_inicio,fecha_final):
       
         try:
                conn = get_db_connection()
                cursor = conn.cursor()

# Convierte las fechas al formato 'yyyy-mm-dd' para la consulta a la API
                fecha_inicio_api = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
                fecha_final_api = datetime.datetime.strptime(fecha_final, '%Y-%m-%d')
                # Realiza el ajuste de un día si es mayor y de un día si es menor
                fecha_inicio_api -= datetime.timedelta(days=1)
                fecha_final_api += datetime.timedelta(days=1)

                fecha_inicio_api = fecha_inicio_api.strftime('%Y-%m-%d')  # La fecha de inicio ajustada
                fecha_final_api = fecha_final_api.strftime('%Y-%m-%d')
                
                cursor.execute("""

  SELECT ht.id_tutoria,concat(u.nombres,' ',u.apellidos) as nombre_completo,ht.cupos,ht.tema,ht.fecha,ht.hora_inicial,ht.hora_final,s.salon,se.sede,txe.estado
FROM `horario_tutorias` ht
inner join usuarios u on ht.id_usuario=u.id_usuario
inner join salones s on s.id_salon=ht.id_salon
inner join sedes se on se.id_sede=s.id_sede
inner join tipoxestado txe on txe.id_tipoxestado=ht.id_estado_tutoria
where ht.id_estado_tutoria=2
and ht.fecha >= STR_TO_DATE(%s, '%Y-%m-%d')
 and ht.fecha <= STR_TO_DATE(%s, '%Y-%m-%d');
    """,(fecha_inicio_api,fecha_final_api))
                result = cursor.fetchall()
                print(result)
                payload = []
                content = {}
                for data in result:
                    fecha_valida=data[4].strftime( '%d-%m-%Y')
                    print(fecha_valida)
                    content = {
                        'codigo': data[0],
                        'nombre_completo':data[1],
                        'cupos':data[2],
                        'tema':data[3],
                        'fecha':fecha_valida,
                        'hora_inicial':data[5],
                        'hora_final':data[6],
                        'salon':data[7],
                        'sede':data[8],
                        'estado':data[9]
                    

                    

                    }
                    print(data[5])
                    payload.append(content)
                    content = {}
                df = pd.DataFrame(payload)
                # Generar un archivo temporal para el informe
                with tempfile.NamedTemporaryFile(delete=True, suffix=".xlsx") as tmp_file:file_name = tmp_file.name
                # Guardar el DataFrame en el archivo temporal
                df.to_excel(file_name, sheet_name="hoja 1", index=False)
                # Devolver el archivo temporal como respuesta
                return FileResponse(file_name, filename="Reporte_tutorias_finalizadas.xlsx")
        
            

         except mysql.connector.Error as err:
            print(err)
            conn.rollback()
         finally:
            conn.close()
    def obtenerListadoPorHorario(id):
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
            where txe.id_tipoxestado=2 and ht.id_tutoria=%s
 
""", (id,))
            data = cursor.fetchall()
            payload = []
            content = {}
            for i in data:
        

                content = {
                     'codigo_tutoria':i[0],
                      'estado_tutoria':i[4],

                       'nombre_estudiante':i[2],
                       'materia':i[5],
                       'numero_documento':i[6],
                       'programa':i[7],
                       'asistencia':i[8],
                       'comentario':i[9]
                }
                payload.append(content)
                content={}
            print(payload)
            df = pd.DataFrame(payload)
                # Generar un archivo temporal para el informe
            with tempfile.NamedTemporaryFile(delete=True, suffix=".xlsx") as tmp_file:file_name = tmp_file.name
                # Guardar el DataFrame en el archivo temporal
            df.to_excel(file_name, sheet_name="hoja 1", index=False)
                # Devolver el archivo temporal como respuesta
            return FileResponse(file_name, filename="Reporte_tutorias_finalizadas.xlsx")
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
       
    
