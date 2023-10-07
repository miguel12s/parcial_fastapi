import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.admin_model import Faculty,TypeDocument,Sede,Capacidad
from fastapi.encoders import jsonable_encoder


class AdminController:
        
    def create_faculty(self, facultad: Faculty):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO facultades (facultad) VALUES (%s)",(facultad.facultad,) )
            conn.commit()
            conn.close()
            return {"resultado": "facultad creada"}
        except mysql.connector.Error as err:
            conn.rollback()
            return ({"error":"la facultad ya existe en el programa"})
        finally:
            conn.close()
        

    def get_faculty(self, id_facultad: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM facultades WHERE id_facultad = %s", (id_facultad,))
            result = cursor.fetchone()          
            if result:
               payload = []
               content = {} 
            
               content={
                    'id':int(result[0]),
                    'facultad':result[1]
               }
               payload.append(content)
            
               json_data = jsonable_encoder(content)  
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Type Document not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_faculties(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM facultades")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'facultad':data[1],
                    
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Programs not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def getTypesDocuments(self):
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipos_documento")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'tipo_documento':data[1],
                    
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Programs not found")  
                
         except mysql.connector.Error as err:
            conn.rollback()
         finally:
            conn.close()
    def  getTypeDocument(self,id_type_document:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipos_documento WHERE id_tipo_documento = %s", (id_type_document,))
            result = cursor.fetchone()          
            if result:
               payload = []
               content = {} 
            
               content={
                    'id':int(result[0]),
                    'tipo_documento':result[1]
               }
               payload.append(content)
            
               json_data = jsonable_encoder(content)  
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Program not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def createTypeDocument(self, typeDocument:TypeDocument):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tipos_documento (tipo_documento) VALUES (%s)",(typeDocument.tipo_documento,) )
            conn.commit()
            conn.close()
            return {"resultado": "tipo de documento  creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            return ({"error":"el tipo de documento  ya existe en el programa"})
        finally:
            conn.close()
        
    
    

    def getSedes(self):
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sedes")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'sede':data[1],
                    
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Sede not found")  
                
         except mysql.connector.Error as err:
            conn.rollback()
         finally:
            conn.close()

    def  getSede(self,id_sede:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sedes WHERE id_sede= %s", (id_sede,))
            result = cursor.fetchone()          
            if result:
               payload = []
               content = {} 
            
               content={
                    'id':int(result[0]),
                    'sede':result[1]
               }
               payload.append(content)
            
               json_data = jsonable_encoder(content)  
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Sede not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def createSede(self, sede:Sede):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO sedes (sede) VALUES (%s)",(sede.sede,) )
            conn.commit()
            conn.close()
            return {"resultado": "sede  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error":"la sede  ya existe en el programa"})
        finally:
            conn.close()


    def getCapacidades(self):
         try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM capacidades")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'capacidad':data[1],
                    
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="capacidad not found")  
                
         except mysql.connector.Error as err:
            conn.rollback()
         finally:
            conn.close()

    def  getCapacidad(self,id_capacidad:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM capacidades WHERE id_capacidad= %s", (id_capacidad,))
            result = cursor.fetchone()          
            if result:
               payload = []
               content = {} 
            
               content={
                    'id':int(result[0]),
                    'capacidad':result[1]
               }
               payload.append(content)
            
               json_data = jsonable_encoder(content)  
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Capacidad not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    def createCapacidad(self, capacidad:Capacidad):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO capacidades (capacidad) VALUES (%s)",(capacidad.capacidad,) )
            conn.commit()
            conn.close()
            return {"resultado": "capacidad  creado"}
        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return ({"error":"la capacidad  ya existe en el programa"})
        finally:
            conn.close()






        

       

##user_controller = UserController()