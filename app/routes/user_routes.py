from fastapi import APIRouter, HTTPException
from controllers.user_controller import *
from models.user_model import User
from typing import List
router = APIRouter(prefix="/user")

nuevo_usuario = UserController()


@router.post("/create_user")
async def create_user(user: User):
    print(user)
    rpta = nuevo_usuario.create_user(user)
    return rpta


@router.get("/get_user/{user_id}")
async def get_user(user_id: int):
    print(user_id)
    rpta = nuevo_usuario.get_user(user_id)
    return rpta

@router.get("/get_users")
async def get_users():
    rpta = nuevo_usuario.get_users()
    return rpta
@router.delete("/user/{id}")

async def deleteUser(id):
    rpta=nuevo_usuario.delete_user(id)
    return rpta


@router.put('/user/{id_user}')

async def updateUser(user:User,id_user):
    rpta=nuevo_usuario.update_user(user,id_user)
    return rpta