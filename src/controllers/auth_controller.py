import mysql.connector
from fastapi import HTTPException
from models.auth import ModelAuth
from schemas.LoginRequest import LoginRequest
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder
from utils.utils import Hasher
from utils.Security import Security
from utils.utils import Hasher

class AuthController:
        
        def login(self,credentials:LoginRequest):

            try:
                conn=get_db_connection()
                cursor=conn.cursor()

                cursor.execute("select contraseña from usuarios where correo=%s",(credentials.email,))
                password_hashed_db=cursor.fetchone()[0]
                hash_verificated=Hasher.verify_password(credentials.password,password_hashed_db)
                if(hash_verificated):
                    cursor.execute("select id_usuario,id_rol,id_estado from usuarios where correo=%s and contraseña=%s",(credentials.email,password_hashed_db))
                    data=cursor.fetchone()
                    
                    if data:
                           json_data=jsonable_encoder(Security.generateToken(data[0]))
                           print(json_data)
                           return {"token":json_data,"id_rol":data[1],"id_estado":data[2],}  
                    else:
                        raise HTTPException(status_code=404, detail="User not found") 
                  
                else:
                 raise HTTPException(status_code=404, detail="User not found") 

 
            except mysql.connector.Error as err:
                conn.rollback()
                return {"error":err}
            finally:
             conn.close()
        def changePassword(self,email:str):
            exist=ModelAuth.existEmail(email)
            if(exist[0]==1):
             password=ModelAuth.get_password()
             password_hash=Hasher.get_password_hash(password)
             ModelAuth.updatePassword(password_hash,email)
             ModelAuth.send_email(exist[1],email,password)
            
    
             return {   "success":"la contraseña ha sido generada porfavor ir al correo"}
            else:
             return {"error":"el correo no existe en el sistema"}
    
