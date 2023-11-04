from config.db_config import get_db_connection

class ModelDocente():
    def verify_hour(horaInicio:str,horaFin:str,fecha:str,id_usuario:int):
        bd=get_db_connection()
        cursor=bd.cursor()
        sql=f"""SELECT count(*) from horario_tutorias ht where ht.hora_inicial="{horaInicio}" and ht.hora_final="{horaFin}" and ht.fecha="{fecha}" and ht.id_usuario={id_usuario} """
        cursor.execute(sql)
        print(sql)
        existe=cursor.fetchone()[0]
        return existe
      
