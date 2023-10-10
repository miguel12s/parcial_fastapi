import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import User
from fastapi.encoders import jsonable_encoder

class UserController:
        
    def create_user(self, user: User):

        try:
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT 
    t.id_tipo_documento,
    f.id_facultad
FROM 
    tipos_documento AS t 
JOIN 
    facultades AS f ON f.facultad =%s
where t.tipo_documento=%s;


""",(user.facultad,user.tipo_documento,))
            result=cursor.fetchone()
            print(result)


            cursor.execute("""
INSERT INTO usuarios (id_rol, id_estado, nombres, apellidos, id_tipo_documento, numero_documento, celular, id_facultad, foto, correo, contraseña)
values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)



""",(user.id_rol,4,user.nombre,user.apellido,result[0],user.numero_documento,user.celular,result[1],user.foto,user.correo,user.contraseña))
            
            id_user=cursor.lastrowid

            conn.commit()

            cursor.execute('insert into camposxusuario (id_usuario,id_campo,dato) values(%s,%s,%s)',(id_user,1,user.facultad))
            conn.commit()
            conn.close()




            return {"resultado": "Usuario creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            print(err)
        finally:
            conn.close()
        

    def get_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id_usuario,nombres,apellidos,numero_documento,foto,f.facultad,td.tipo_documento,celular,correo,contraseña,txe.estado,r.rol FROM usuarios u join tipos_documento td on u.id_tipo_documento=td.id_tipo_documento join facultades f on u.id_facultad=f.id_facultad join tipoxestado txe on txe.id_tipoestado=u.id_estado join roles r on r.id_rol=u.id_rol where id_usuario=%s", (user_id,))
            result = cursor.fetchone()
            print(result)
            payload = []
            content = {} 
            
            content={
                 'id':result[0],
                    'nombre':result[1],
                    'apellido':result[2],
                    'numero_documento':result[3],
                    'foto':result[4],
                    'facultad':result[5],
                    'tipo_documento':result[6],
                    'celular':result[7],
                    'correo':result[8],
                    'contraseña':result[9],
                    'id_estado':result[10],
                    'id_rol':result[11]  
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
            cursor.execute("SELECT id_usuario,nombres,apellidos,numero_documento,foto,f.facultad,td.tipo_documento,celular,correo,contraseña,txe.estado,r.rol FROM usuarios u join tipos_documento td on u.id_tipo_documento=td.id_tipo_documento join facultades f on u.id_facultad=f.id_facultad join tipoxestado txe on txe.id_tipoestado=u.id_estado join roles r on r.id_rol=u.id_rol")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_rol':data[11],
                    'id_estado':data[10],
                    'nombre':data[1],
                    'apellido':data[2],
                    'tipo_documento':data[6],

                    'numero_documento':data[3],
                    'celular':data[7],
                    'facultad':data[5],

                    'foto':data[4],
                    
                    'correo':data[8],
                    'contraseña':data[9],
                    
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
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
    def update_user(self,user:User,id_user:int):
        try:
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT 
          t.id_tipo_documento,
         f.id_facultad
         FROM 
        tipos_documento AS t 
JOIN 
    facultades AS f ON f.facultad =%s
where t.tipo_documento=%s;


""",(user.facultad,user.tipo_documento,))
            result=cursor.fetchone()
            print(result)


            cursor.execute("""
update usuarios set id_rol=%s, id_estado=%s, nombres=%s, apellidos=%s, id_tipo_documento=%s, numero_documento=%s, celular=%s, id_facultad=%s, foto=%s, correo=%s, contraseña=%s where id_usuario=%s




""",(user.id_rol,4,user.nombre,user.apellido,result[0],user.numero_documento,user.celular,result[1],user.foto,user.correo,user.contraseña,id_user,))
            

            conn.commit()
            cursor.execute('update camposxusuario set dato=%s where id_usuario=%s',(user.facultad,id_user))
            conn.commit()
            conn.close()




            return {"resultado": "Usuario actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            print(err)
        finally:
            conn.close()
    
    
       

##user_controller = UserController()