from fastapi import APIRouter,Depends, Request
from typing import List
from controllers.faculty_controller import *
from models.Faculty import Faculty
from utils.Security import Security

facultad=APIRouter()

nueva_facultad=FacultyController()

@facultad.post("/facultad",status_code=201)
async def create_faculty(facultad:Faculty):
    rpta = nueva_facultad.create_faculty(facultad)
    return rpta


@facultad.get("/facultad/{id_faculty}",response_model=Faculty)
async def get_faculty(id_faculty: int):
    rpta = nueva_facultad.get_faculty(id_faculty)
    return rpta

@facultad.get("/facultades",dependencies=[Depends(Security.verify_token)])
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

