import random
import requests
from config.db_config import get_db_connection
import mysql.connector
class ModelAuth():
    def existEmail(email):
        try:
                conn=get_db_connection()
                cursor=conn.cursor()

                cursor.execute("select count(*),concat(nombres,' ',apellidos) from usuarios where correo=%s",(email,))
                existEmail=cursor.fetchone()
                return existEmail
        except mysql.connector.Error as err:
                conn.rollback()
                return {"error":err}
        finally:
             conn.close()
    def updatePassword(password_hash:str,email):
        try:
                conn=get_db_connection()
                cursor=conn.cursor()

                cursor.execute("update usuarios set contraseña=%s  where correo=%s",(password_hash,email))
                conn.commit()
                conn.close()
                
        except mysql.connector.Error as err:
                conn.rollback()
                return {"error":err}
        finally:
             conn.close()
    def get_password():
        minusculas="abcdefghijklmnopqrstuvwxyz"
        mayusculas="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        simbolos="@()[]{}*;/-_¿?!¡$"
        base=minusculas+mayusculas+simbolos
        longitud_contraseña=10
        password=random.sample(base,longitud_contraseña)
        passwordComplete="".join(password)
        return passwordComplete
    def send_email(full_name,email,password):
             email_data = {
                "subject": "Cambio de contraseña",
                "message": f"Estimado {full_name},\n\nLe damos la bienvenida a la Universidad. Su contraseña ha sido cambiada con éxito.La contraseña es la siguiente {password} \nEquipo de Admisiones",
                "to_email": email

                }
             response=requests.post('http://127.0.0.1:8300/send-email',json=email_data)
             print(response)
            #  if(response.status_code==200):
            #     return {"success":"el correo ha sido enviado"}
            #  else:
            #        return {"error":"el correo no se pudo enviar"}
         
         