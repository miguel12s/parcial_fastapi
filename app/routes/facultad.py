from fastapi import APIRouter
from typing import List
from controllers.faculty_controller import *
from models.Faculty import Faculty

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

@facultad.get("/facultades")
async def get_faculties():
    rpta = nueva_facultad.get_faculties()
    return rpta