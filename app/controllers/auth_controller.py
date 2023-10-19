import mysql.connector
from fastapi import HTTPException
from models.LoginRequest import LoginRequest
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder
from utils.utils import Hasher
class AuthController:
        
        def login(self,credentials:LoginRequest):

            try:
                conn=get_db_connection()
                cursor=conn.cursor()

                cursor.execute("select contraseña from usuarios where correo=%s",(credentials.email,))
                password_hashed_db=cursor.fetchone()[0]
                print(password_hashed_db)
                hash_verificated=Hasher.verify_password(credentials.password,password_hashed_db)
                if(hash_verificated):
                    cursor.execute("select id_usuario,id_rol,id_estado from usuarios where correo=%s and contraseña=%s",(credentials.email,password_hashed_db))
                    data=cursor.fetchone()
                    content={
                        "id_usuario":data[0],
                        "id_rol":data[1],
                        "id_estado":data[2]
                    }
                    if data:
                           json_data=jsonable_encoder(content)
                           print(json_data)
                           return json_data    
                    else:
                        raise HTTPException(status_code=404, detail="User not found") 
                  
                else:
                 raise HTTPException(status_code=404, detail="User not found") 

 
            except mysql.connector.Error as err:
                conn.rollback()
                return {"error":err}
            finally:
             conn.close()
