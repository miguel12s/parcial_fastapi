import mysql.connector
from models.Notification import Notification
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder

class AdminController:
        
        def createNotifiaction(self,contactForm:Notification):
                
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO contact (nombres,apellidos,correo,celular,mensaje) VALUES (%s,%s,%s,%s,%s)", (contactForm.nombre,contactForm.apellido,contactForm.correo,contactForm.celular,contactForm.mensaje))
            conn.commit()
            conn.close()
            return {"resultado": "Notificacion  creada"}
         except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "ocurrio un error al realizar la consulta"})
         finally:
            conn.close()
