import io
import mysql.connector
from fastapi import HTTPException, UploadFile
from config.db_config import get_db_connection
from schemas.user_model import User, updateUser
from fastapi.encoders import jsonable_encoder
from utils.utils import Hasher
from models.admin import ModelAdmin
from schemas.changePassword import ChangePassword
import datetime
import pandas as pd


modelAdmin=ModelAdmin()

class UserController:
        

    def cambiarContraseña(self,changedPassword:ChangePassword,user_id:int):
        try:
          hashed_password=ModelAdmin.obtenerContraseña(user_id)
          if(Hasher.verify_password(changedPassword.contraseña_actual,hashed_password)):
            rpta=ModelAdmin.cambiarContraseña(changedPassword,user_id)
            return rpta
          return {"error":"la contraseña no se encuentra en el sistema"}
        except Exception as e: 
         print(e)
         raise HTTPException(status_code=400, detail="Error al procesar el archivo")
    

    def create_user(self, user: User):

        try:    
            fecha_actual=datetime.datetime.now()
            fecha_sin_microsegundos=fecha_actual.replace(microsecond=0)

            fecha_formateada = fecha_sin_microsegundos.strftime("%Y-%m-%d %H:%M:%S")
            print(fecha_formateada)
            conn = get_db_connection()
            cursor = conn.cursor()
            print(fecha_formateada)

            cursor.execute("""
INSERT INTO usuarios (id_rol, id_estado, nombres, apellidos, id_tipo_documento, numero_documento, celular,  correo, contraseña)
values(%s,%s,%s,%s,%s,%s,%s,%s,%s)



""",(user.id_rol,4,user.nombres,user.apellidos,user.id_tipo_documento,user.numero_documento,user.celular,user.correo,Hasher.get_password_hash(user.contraseña)))
            
            id_user=cursor.lastrowid
            conn.commit()

            cursor.execute('insert into camposxusuario (id_usuario,id_campo,dato) values(%s,%s,%s)',(id_user,1,str(user.id_programa)))
            conn.commit()
            cursor.execute("""SELECT fxp.id_fxp FROM `facultadxprograma` fxp join facultades f on fxp.id_facultad=f.id_facultad join programas p on fxp.id_programa=p.id_programa

where p.id_programa=%s and f.id_facultad=%s """,(user.id_programa,user.id_facultad))
            id_fxp=cursor.fetchone()[0]

            cursor.execute('INSERT INTO `fpxusuario`(`id_fxp`, `id_usuario`) VALUES (%s,%s)',(id_fxp,id_user))
            conn.commit()
            cursor.execute('INSERT INTO `registro_actividad`( `id_tipo_actividad`, `id_usuario`, `fecha_hora`, `ubicacion_actividad`) VALUES (%s,%s,%s,%s) ',(2,id_user,fecha_formateada,'crear usuario'))
            conn.commit()
            conn.close()






            return {"success": "Usuario creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return {"error":err}
        finally:
            conn.close()
        

    def get_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            # select u.id_usuario,u.nombres,u.apellidos,td.tipo_documento,f.facultad, u.numero_documento,u.celular,u.foto,u.correo,u.contraseña from  usuarios u join tipos_documento td on u.id_tipo_documento=td.id_tipo_documento   join facultades f on f.id_facultad=fxp.id_facultad  join facultadxprograma fxp on fxp.id_facultad=7 join fpxusuario  fpx on fpx.id_usuario=u.id_usuario    WHERE u.id_usuario=11
            sql="SELECT  u.id_usuario,u.nombres,u.apellidos,t.tipo_documento,  u.numero_documento,f.facultad,p.programa,u.celular,u.foto,u.correo,u.contraseña,txe.estado FROM `usuarios` u  join tipos_documento t on u.id_tipo_documento=t.id_tipo_documento join fpxusuario facusu on facusu.id_usuario=u.id_usuario     join facultadxprograma fxp on fxp.id_fxp=facusu.id_fxp join facultades f on f.id_facultad=fxp.id_facultad join programas p on p.id_programa=fxp.id_programa join tipoxestado txe on txe.id_tipoxestado=u.id_estado   WHERE u.id_usuario=%s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
            print(result)
            payload = []
            content = {} 
            
            content={
                 'id':result[0],
                    'nombres':result[1],
                    'apellidos':result[2],
                    'tipo_documento':result[3],
                    'numero_documento':result[4],
                    'facultad':result[5],
                    'programa':result[6],
                    'celular':result[7],
                    'foto':result[8],
                    'correo':result[9],
                    'contraseña':result[10],
                    'estado':result[11]
                    # 'id_estado':result[10],
                    # 'id_rol':result[11]  
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)  
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT  u.id_usuario,u.nombres,u.apellidos,t.tipo_documento,  u.numero_documento,f.facultad,p.programa,u.celular,u.foto,u.correo,u.contraseña FROM `usuarios` u  join tipos_documento t on u.id_tipo_documento=t.id_tipo_documento join fpxusuario facusu on facusu.id_usuario=u.id_usuario     join facultadxprograma fxp on fxp.id_fxp=facusu.id_fxp join facultades f on f.id_facultad=fxp.id_facultad join programas p on p.id_programa=fxp.id_programa")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'apellido':data[2],
                    'tipo_documento':data[3],
                    'numero_documento':data[4],
                    'facultad':data[5],
                    'programa':data[6],
                    'celular':data[7],
                    'foto':data[8],
                    'correo':data[9],
                    'contraseña':data[10],
                    
                }
                payload.append(content)
                content = {}
            conn.close()
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                return {"error":"no hay usuarios"}
                
        except mysql.connector.Error as err:
            conn.rollback()

        finally:
            conn.close()
    def delete_user(self,id_user:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("delete from usuarios where id_usuario=%s",(int(id_user),))
            conn.commit()
            conn.close()
            return {"success":"usuario eliminado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def update_user(self,user:updateUser,id_user:int):
        try:
            print(user)
            conn = get_db_connection()
            cursor = conn.cursor()

            
            cursor.execute("""SELECT 
          td.id_tipo_documento
        ,f.id_facultad
        ,p.id_programa
        ,txe.id_tipoxestado
         FROM 
        usuarios u 
JOIN facultades AS f ON f.facultad =%s
join programas p on p.programa=%s
join tipos_documento td on td.tipo_documento=%s
join tipoxestado txe on txe.estado=%s


""",(user.facultad,user.programa,user.tipo_documento,user.estado))
            result=cursor.fetchone()
            id_fxp=ModelAdmin.obtenerid(result)
            ModelAdmin.updateUser(user,result,id_user)
            ModelAdmin.updateFacultad(id_fxp,id_user)
            
            

#             conn.commit()
           


            

            return {"success": "Usuario actualizado"}
        except mysql.connector.Error as err:
            print(err)

            conn.rollback()
        finally:
            conn.close()
    async def insertMultipleUsers(self, file: UploadFile):
     try:
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=422, detail="El archivo no es un CSV válido")

        payload=[]
        file_content=await file.read()
        df = pd.read_csv(io.BytesIO(file_content),encoding='latin-1')
        # Procesa el DataFrame df, por ejemplo, imprime sus contenidos

        for index, row in df.iterrows():
            user_data = row.to_dict()
            data=user_data['rol;nombre;apellido;tipodocumento;numerodocumento;celular;correo;password;facultad;programa'].split(';')
            content={
                "rol":data[0],
                "nombre":data[1],
                "apellido":data[2],
                "tipo_documento":data[3],
                "numero_documento":data[4],
                "celular":data[5],
                "correo":data[6],
                "password":data[7],
                "facultad":data[8],
                "programa":data[9]
            }
            payload.append(content)
            content={}
        res= await ModelAdmin.createMultipleUsers(payload)
        print(res)

        return {"message": res}
     except Exception as e: 
        print(e)
        raise HTTPException(status_code=400, detail="Error al procesar el archivo")
    def get_docentes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT distinct  u.id_usuario,u.nombres,u.apellidos,t.tipo_documento,  u.numero_documento,f.facultad,p.programa,u.celular,u.foto,u.correo,u.contraseña FROM `usuarios` u  join tipos_documento t on u.id_tipo_documento=t.id_tipo_documento join fpxusuario facusu on facusu.id_usuario=u.id_usuario     join facultadxprograma fxp on fxp.id_fxp=facusu.id_fxp join facultades f on f.id_facultad=fxp.id_facultad join programas p on p.id_programa=fxp.id_programa where u.id_rol=2 and u.id_estado=4 group by u.id_usuario ")
            
            result = cursor.fetchall()
            print(result)
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'apellido':data[2],
                    'tipo_documento':data[3],
                    'numero_documento':data[4],
                    'facultad':data[5],
                    'programa':data[6],
                    'celular':data[7],
                    'foto':data[8],
                    'correo':data[9],
                    'contraseña':data[10],
                    
                }
                payload.append(content)
                content = {}
            conn.close()
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                return {"error":"no hay usuarios"}
                
        except mysql.connector.Error as err:
            conn.rollback()

        finally:
            conn.close()

    

    
       

##user_controller = UserController()