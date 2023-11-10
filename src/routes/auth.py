from fastapi import APIRouter
from controllers.auth_controller import AuthController
from schemas.LoginRequest import LoginRequest
from controllers.campoad_controller import *
from pydantic import BaseModel
class Email(BaseModel):
    email:str
auth=APIRouter(prefix="/auth")

new_auth=AuthController()

# oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/token")

# SECRET_KEY =config('SECRET_KEY')
# ALGORITHM = config('ALGORITHM')
# ACCESS_TOKEN_EXPIRE_MINUTES = config('ACCESS_TOKEN_EXPIRE_MINUTES',default=30,cast=int)


@auth.post('/login')

def login(credentials:LoginRequest):
    rpta=new_auth.login(credentials)
    return rpta
@auth.post('/send-email')
def sendEmail(email:Email):
    print(email)
    rpta=new_auth.changePassword(email.email)
    return rpta
    


