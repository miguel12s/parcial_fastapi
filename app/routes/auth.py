from fastapi import APIRouter,Depends,HTTPException,status
from datetime import datetime,timedelta
from controllers.auth_controller import AuthController
from models.LoginRequest import LoginRequest
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import JWTError,jwt
from pydantic import BaseModel
from typing import Annotated
from passlib.context import CryptContext
from decouple import config
from controllers.campoad_controller import *
from utils.utils import Hasher
from models.Token import Token,TokenData
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

