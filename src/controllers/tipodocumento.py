import mysql.connector
from fastapi import HTTPException
from schemas.TypeDocument import TypeDocument
from config.db_config import get_db_connection
from fastapi.encoders import jsonable_encoder

class TipoDocumentoController:
    def getTypesDocuments(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipos_documento")
            result = cursor.fetchall()
            payload = []
            content = {}
            for data in result:
                content = {
                    'id': data[0],
                    'tipo_documento': data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            print(json_data)
            conn.close()
            if result:
                return {"resultado": json_data}
            else:
                raise HTTPException(
                    status_code=404, detail="Programs not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def getTypeDocument(self, id_type_document: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM tipos_documento WHERE id_tipo_documento = %s", (id_type_document,))
            result = cursor.fetchone()
            if result:
                payload = []
                content = {}

                content = {
                    'id': int(result[0]),
                    'tipo_documento': result[1]
                }
                payload.append(content)

                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(
                    status_code=404, detail="Program not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def createTypeDocument(self, typeDocument: TypeDocument):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tipos_documento (tipo_documento) VALUES (%s)", (typeDocument.tipo_documento,))
            conn.commit()
            conn.close()
            return {"resultado": "tipo de documento  creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            return ({"error": "el tipo de documento  ya existe en el programa"})
        finally:
            conn.close()
    def update_type_document(self,data:TypeDocument,id_type_document):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""update tipos_documento set tipo_documento=%s where id_tipo_documento=%s""",(data.tipo_documento,id_type_document))
            conn.commit()
            conn.close()
            return {"success":"el tipo de documento ha sido actualizada"}
            

        except mysql.connector.Error as err:
            print(err)
            conn.rollback()
            return {"error":"el tipo de documento se encuentra registrada en el programa"}
        finally:
            conn.close()