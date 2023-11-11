import mysql.connector
from models.auth import ModelAuth
from schemas.Notification import Notification, NotificationSend
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
      def getNotifications(self):
                
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
         select id_contac, concat(nombres,' ',apellidos),correo,celular,mensaje from contact where id_estado=18
""")
            result=cursor.fetchall()
            conn.close()
            payload=[]
            content={}
            for data in result:
               content={
                  "id":data[0],
                  "nombre_completo":data[1],
                  "correo":data[2],
                  "celular":data[3],
                  "mensaje":data[4],
               }
               payload.append(content)
            json_data=jsonable_encoder(payload)
            if result:

             return {"resultado":json_data}
            return {"error":"no existe ninguna notificacion "}
         except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "ocurrio un error al realizar la consulta"})
         finally:
            conn.close()

      def getNotification(self,id):
                
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
         select id_contac, concat(nombres,' ',apellidos),correo,celular,mensaje from contact where id_estado=18 and  id_contac=%s
""",(id,))
            data=cursor.fetchone()
            conn.close()
            content={
                  "id":data[0],
                  "nombre_completo":data[1],
                  "correo":data[2],
                  "celular":data[3],
                  "mensaje":data[4],
               }
            print(content)
            if data:

             return content
            return {"error":"no existe ninguna notificacion "}
         except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "ocurrio un error al realizar la consulta"})
         finally:
            conn.close()
      def sendResponse(self,response:NotificationSend,id_contact:int):
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                update contact set respuesta=%s,id_estado=%s where id_contac=%s
         
""",(response.respuesta,17,id_contact))
            conn.commit()
            conn.close()
            ModelAuth.send_response(response)
            
            return {"error":"no existe ninguna notificacion "}
         except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "ocurrio un error al realizar la consulta"})
         finally:
            conn.close()

      


      def getNotificationsFinish(self):
                
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
         select id_contac, concat(nombres,' ',apellidos),correo,celular,mensaje from contact where id_estado=17
""")
            result=cursor.fetchall()
            conn.close()
            payload=[]
            content={}
            for data in result:
               content={
                  "id":data[0],
                  "nombre_completo":data[1],
                  "correo":data[2],
                  "celular":data[3],
                  "mensaje":data[4],
               }
               payload.append(content)
            json_data=jsonable_encoder(payload)
            if result:

             return {"resultado":json_data}
            return {"error":"no existe ninguna notificacion "}
         except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "ocurrio un error al realizar la consulta"})
         finally:
            conn.close()

      def getNotificationFinish(self,id):
                
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
         select id_contac, concat(nombres,' ',apellidos),correo,celular,mensaje,respuesta from contact where id_estado=17 and  id_contac=%s
""",(id,))
            data=cursor.fetchone()
            conn.close()
            content={
                  "id":data[0],
                  "nombre_completo":data[1],
                  "correo":data[2],
                  "celular":data[3],
                  "mensaje":data[4],
                  "respuesta":data[5]
               }
            print(content)
            if data:

             return content
            return {"error":"no existe ninguna notificacion "}
         except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error": "ocurrio un error al realizar la consulta"})
         finally:
            conn.close()
      
