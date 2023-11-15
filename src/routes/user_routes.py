from fastapi import APIRouter,Request
from controllers.user_controller import *
from schemas.user_model import User,updateUser
from utils.Security import Security
router = APIRouter(prefix="/user")

nuevo_usuario = UserController()


@router.post("/create_user")
async def create_user(user: User):
    print(user)
    rpta = nuevo_usuario.create_user(user)
    return rpta


@router.get("/get_user")
async def get_user(request:Request):
    headers=request.headers
    payload=Security.verify_token(headers=headers)
    user_id=payload['id_usuario']
    print(user_id)
    rpta = nuevo_usuario.get_user(user_id)
    return rpta

@router.get("/get_users")
async def get_users():
    rpta = nuevo_usuario.get_users()
    return rpta['resultado']


@router.get("/get_docentes")
async def get_users():
    rpta = nuevo_usuario.get_docentes()
    return rpta['resultado']
# @router.delete("/user/{id}")

# async def deleteUser(id):
#     rpta=nuevo_usuario.delete_user(id)
#     return rpta


@router.get('/{id_user}')

async def updateUserf(id_user):
    rpta=nuevo_usuario.get_user(id_user)
    return rpta

@router.put('/{id_user}')

async def updatefUser(user:updateUser,id_user):
    rpta=nuevo_usuario.update_user(user,id_user)
    return rpta



@router.post('/multiple-users')
async def createMultipleUsers(formdata:UploadFile):
    try:
        rpta=await nuevo_usuario.insertMultipleUsers(formdata)
        return rpta
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400,detail=e)


@router.post('/cambiar-password')

def cambiarContraseña(changePassword:ChangePassword,request:Request):
    headers=request.headers
    payload=Security.verify_token(headers)
    user_id=payload['id_usuario']
    print(user_id)
    rpta = nuevo_usuario.cambiarContraseña(changePassword,user_id)
    return rpta



