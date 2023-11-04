from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from utils.utils import Hasher
from schemas.Materia import Materia
from config.db_config import get_db_connection
import mysql.connector

class ModelAdmin:
    def getMaterias():
        try:
            print('entras')
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM materias")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'materia': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="materia not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def getMateria(id_materia: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM materias WHERE id_materia= %s", (id_materia,))
            result = cursor.fetchone()
            if result:
                
                content = {}

                content = {
                    'id': int(result[0]),
                    'materia': result[1]
                }
                
                print(content)
                json_data = jsonable_encoder(content)
                print(json_data)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="materia not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def createMateria( materia: Materia):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO materias (materia) VALUES (%s)", (materia.materia,))
            conn.commit()
            conn.close()
            return {"resultado": "materia  creada"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "la materia  ya existe en el programa"})
        finally:
            conn.close()
    async def createMultipleUsers(users):
        try:

            conn = get_db_connection()
            cursor = conn.cursor()
            
            for user in users:
                 # Realiza la búsqueda para obtener los IDs correspondientes
                cursor.execute("""
                    SELECT r.id_rol, td.id_tipo_documento
                    FROM roles r
                    JOIN tipos_documento td ON td.tipo_documento = %s
                    WHERE r.rol = %s
                """, (user['tipo_documento'], user['rol']))
                result = cursor.fetchone()

                if result:
                    id_rol, id_tipo_documento = result
                    cursor.execute("""
                        INSERT INTO usuarios (id_rol, id_estado, nombres, apellidos, id_tipo_documento, numero_documento, celular, correo, contraseña)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (id_rol, 4, user['nombre'], user['apellido'], id_tipo_documento, user['numero_documento'], user['celular'], user['correo'], Hasher.get_password_hash(user['password'])))
                    id_user=cursor.lastrowid
                    ## insertar facultad y programa en usuario
                    conn.commit()
                    cursor.execute("""SELECT fxp.id_fxp FROM `facultadxprograma` fxp join facultades f on fxp.id_facultad=f.id_facultad join programas p on fxp.id_programa=p.id_programa 
where f.id_facultad=(select f2.id_facultad from facultades f2 where  f2.facultad=%s ) and p.id_programa=(select p2.id_programa from programas p2 where p2.programa=%s) """,(user['facultad'],user['programa']))
                    id_fxp=cursor.fetchone()[0]
                    

                    cursor.execute('INSERT INTO `fpxusuario`(`id_fxp`, `id_usuario`) VALUES (%s,%s)',(id_fxp,id_user))
                
                    
                    conn.commit()
           
            return {"resultado": "Usuarios creados"}
        
            
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "la materia  ya existe en el programa"})
        finally:
            cursor.close()
            conn.close()