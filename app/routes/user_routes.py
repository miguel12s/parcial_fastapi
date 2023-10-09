from fastapi import APIRouter, HTTPException
from controllers.user_controller import *
from models.user_model import User
from typing import List
router = APIRouter()

nuevo_usuario = UserController()


@router.post("/create_user")
async def create_user(user: User):
    rpta = nuevo_usuario.create_user(user)
    return rpta


@router.get("/get_user/{user_id}",response_model=User)
async def get_user(user_id: int):
    rpta = nuevo_usuario.get_user(user_id)
    return rpta

@router.get("/get_users/",response_model=List[User])
async def get_users():
    rpta = nuevo_usuario.get_users()
    return rpta['resultado']
@router.delete("/user/{id}")

async def deleteUser(id):
    rpta=nuevo_usuario.delete_user(id)
    return rpta