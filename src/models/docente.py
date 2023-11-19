from config.db_config import get_db_connection
from schemas.Horario import Horario

class ModelDocente():
    def verify_hour(horaInicio:str,horaFin:str,fecha:str,id_usuario:int):
        bd=get_db_connection()
        cursor=bd.cursor()
        sql=f"""SELECT count(*) from horario_tutorias ht where ht.hora_inicial="{horaInicio}" and ht.hora_final="{horaFin}" and ht.fecha="{fecha}" and ht.id_usuario={id_usuario} """
        cursor.execute(sql)
        existe=cursor.fetchone()[0]
        return existe
    def createHorario(horario:Horario,id_usuario:int,id_fpxm:int):
        bd=get_db_connection()
        cursor=bd.cursor()
        cursor.execute("""
        INSERT INTO horario_tutorias (id_fpxm, id_salon, id_usuario, id_estado_tutoria, cupos, tema, fecha, hora_inicial, hora_final)
                VALUES (%s,%s,%s,%s,%s,%s,%s, %s,%s)

                            


    """,(id_fpxm, horario.id_salon,id_usuario,6,horario.cupos,horario.tema,horario.fecha,horario.hora_inicial,horario.hora_final))
        bd.commit()
        cursor.close()
      
