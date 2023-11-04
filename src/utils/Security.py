import datetime
import pytz
import jwt


class Security():
    tz=pytz.timezone("America/Bogota")

    @classmethod
    def generateToken(cls,id_usuario):
        payload={
            'iat':datetime.datetime.now(tz=cls.tz),
            'exp':datetime.datetime.now(tz=cls.tz)+datetime.timedelta(hours=1),
            'id_usuario':id_usuario,
            

        }
        return jwt.encode(payload=payload,key="secret_key"  ,algorithm="HS256")
    @classmethod
    def verify_token(cls,headers):
        if 'Authorization' in headers:
         print('entras')
         authorization=headers['Authorization']
         token=authorization.split(' ')[1]
         print(token)
         try:
            payload=jwt.decode(token,'secret_key',algorithms='HS256')
            return payload
         except (jwt.ExpiredSignatureError):
            return False
        return False
    
    @classmethod
    def renew_token(cls, token):
        try:
            payload = jwt.decode(token, 'secret_key', algorithms='HS256')
            new_token = cls.generate_token(payload['id_usuario'])
            return new_token
        except jwt.ExpiredSignatureError:
            return None