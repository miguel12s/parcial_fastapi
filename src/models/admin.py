from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from schemas.changePassword import ChangePassword
from schemas.user_model import updateUser
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
            return {"success": "materia  creada"}
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
            return ({"error": "el correo o el numero de documento ya se encuentra registrado "})
        finally:
            cursor.close()
            conn.close()
    def obtenerContraseña(user_id:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "select contraseña from usuarios where id_usuario=%s", (user_id,))
            result = cursor.fetchone()[0]
            if result:
                return result
            else:
                raise HTTPException(
                    status_code=404, detail="el usuario no esta autenticado")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def cambiarContraseña(changedPassword:ChangePassword,user_id:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "update usuarios set contraseña=%s  where id_usuario=%s", (Hasher.get_password_hash(changedPassword.contraseña_nueva),user_id))
            conn.commit()
        
            return {"message":"la contraseña ha sido cambiada"}
           

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def updateMateria(materia:Materia,id:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "update materias set materia=%s  where id_materia=%s",(materia.materia,id))
            conn.commit()
        
            return {"success":"la materia ha sido actualizada"}
           

        except mysql.connector.Error as err:
            
            conn.rollback()
            return {"error":"la materia ya existe en el sistema"}
        finally:
            conn.close()
    def obtenerid(result):
            conn = get_db_connection()
            cursor = conn.cursor()
            print(result)
            sql=f"""select fxp.id_fxp from facultadxprograma fxp where fxp.id_facultad={result[1]} and fxp.id_programa={result[2]}"""
            cursor.execute(sql)
            print(sql)
            # 
            id_fxp=cursor.fetchone()[0]
            return id_fxp
    def updateUser(user:updateUser,result,id_user:int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
update usuarios set id_estado=%s, nombres=%s, apellidos=%s, id_tipo_documento=%s, numero_documento=%s, celular=%s, correo=%s where id_usuario=%s




""",(result[3],user.nombres,user.apellidos,result[0],user.numero_documento,user.celular,user.correo,id_user))
        conn.commit()
        conn.close()
    def updateFacultad(id_fxp,id_user):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
update fpxusuario set id_fxp=%s where id_usuario=%s



""",(id_fxp,id_user))
        conn.commit()
        conn.close()
