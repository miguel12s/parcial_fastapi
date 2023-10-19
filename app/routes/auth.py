from fastapi import APIRouter
from controllers.auth_controller import AuthController
from models.LoginRequest import LoginRequest
from controllers.campoad_controller import *


auth=APIRouter(prefix='/auth')

new_auth=AuthController()


@auth.post('/login')

def login(credentials:LoginRequest):
    rpta=new_auth.login(credentials)
    return rpta

