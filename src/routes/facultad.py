from fastapi import APIRouter,Depends, Request
from typing import List
from controllers.faculty_controller import *
from schemas.Faculty import Faculty, FacultyxUser
from utils.Security import Security

facultad=APIRouter()

nueva_facultad=FacultyController()

@facultad.post("/facultad",status_code=201)
async def create_faculty(facultad:Faculty):
    rpta = nueva_facultad.create_faculty(facultad)
    return rpta


@facultad.put("/facultad/{id_faculty}")
async def create_faculty(facultad:Faculty,id_faculty):
    rpta = nueva_facultad.update_faculty(facultad,id_faculty)
    return rpta

@facultad.get("/facultad/{id_faculty}",response_model=Faculty)
async def get_faculty(id_faculty: int):
    rpta = nueva_facultad.get_faculty(id_faculty)
    return rpta

@facultad.get("/facultades")
async def get_faculties():
    try:
     rpta = nueva_facultad.get_faculties()
     return rpta

    except Exception as e:
       return {"error":e}

@facultad.get('/facultad-user')
async def get_faculty_user(request:Request):
    headers=request.headers
    payload=Security.verify_token(headers)
    id_usuario=payload['id_usuario']
    rpta = nueva_facultad.get_faculty_user(id_usuario)
    print(rpta)
    return rpta

@facultad.get('/facultad-user-docente/{id_usuario}')

def facultadUserDocente(id_usuario):
   rpta=nueva_facultad.getFacultadUserDocente(id_usuario)
   return rpta

@facultad.get('/facultad-users')

def getFacultadUser():
   rpta=nueva_facultad.getFacultadUser()
   return rpta

@facultad.get('/facultadxusuario/{id_usuario}')

def getFacultadUser(id_usuario):
   rpta=nueva_facultad.getFacultadxUsuario(id_usuario)
   return rpta


@facultad.get('/facultadxusuarios/{id_fpxusuario}')


def getFacultadxUsuario(id_fpxusuario:int):
   rpta=nueva_facultad.getFacultadxUsuarioForId(id_fpxusuario)
   return rpta


@facultad.put('/facultadxusuarios/{id_fpxusuario}')


def getFacultadxUsuario(id_fpxusuario:int,data:FacultyxUser):
   print(data)
   rpta=nueva_facultad.updateFacultadxUsuarioForId(id_fpxusuario,data)
   return rpta