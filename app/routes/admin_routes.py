from fastapi import APIRouter, HTTPException
from controllers.admin_controller import *
from models.admin_model import  Program,Faculty,typeDocument
from typing import List




router = APIRouter()

nuevo_admin = AdminController()


@router.post("/facultad")
async def create_user(facultad:Faculty):
    rpta = nuevo_admin.create_faculty(facultad)
    return rpta


@router.get("/facultad/{id_faculty}",response_model=Faculty)
async def get_user(id_faculty: int):
    rpta = nuevo_admin.get_faculty(id_faculty)
    return rpta

@router.get("/facultades",response_model=List[Faculty])
async def get_users():
    rpta = nuevo_admin.get_faculties()
    return rpta['resultado']

@router.get('/tipoDocumento/{id_type_document}',response_model=typeDocument)


async def getTypeDocument(typeDocument:typeDocument):
    rpta=nuevo_admin.getTypeDocument()
    return rpta


@router.get('/tipoDocumentos')

async def getTypesDocuments():
    rpta=nuevo_admin.getTypesDocuments()
    return rpta
