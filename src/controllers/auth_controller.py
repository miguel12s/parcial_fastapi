import mysql.connector
from fastapi import HTTPException
from models.auth import ModelAuth
from schemas.LoginRequest import LoginRequest
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder
from utils.utils import Hasher
from utils.Security import Security
from utils.utils import Hasher
from models.auth import ModelAuth
class AuthController:
        
        def login(self,credentials:LoginRequest):

            try:
                password_hashed_db=ModelAuth.get_password_hash(credentials)
                if password_hashed_db==None:
                    return {"errorUser":"Usuario no encontrado"}
                hash_verificated=Hasher.verify_password(credentials.password,password_hashed_db)
                if(hash_verificated):
                    data=ModelAuth.getUserAuthenticated(credentials,password_hashed_db)
                    if data:
                           json_data=jsonable_encoder(Security.generateToken(data[0]))
                           print(json_data)
                           return {"token":json_data,"id_rol":data[1],"id_estado":data[2],}  
                    else:
                        return {"error":"correo o contraseña incorrecta"}

                       # raise HTTPException(status_code=404, detail="User not found") 
                else:
                    return {"error":"correo o contraseña incorrecta"}
                #    raise HTTPException(status_code=404, detail="User not found") 
               

 
            except mysql.connector.Error as err:
                
                return {"error":err}
            
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
    
