from fastapi import APIRouter, HTTPException
from controllers.admin_controller import *
from models.admin_model import  Program,Faculty,TypeDocument,Sede,Capacidad
from typing import List




router = APIRouter()

nuevo_admin = AdminController()

## tabla facultad
@router.post("/facultad",status_code=201)
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


##tabla  tipo documentos
@router.get('/tipoDocumento/{id_type_document}',response_model=TypeDocument)


async def getTypeDocument(id_type_document):
    rpta=nuevo_admin.getTypeDocument( id_type_document)
    return rpta


@router.get('/tipoDocumento',response_model=List[TypeDocument])

async def getTypesDocuments():
    rpta=nuevo_admin.getTypesDocuments()
    return rpta['resultado']



@router.post('/tipoDocumento',status_code=201)


async def createTypeDocument(typeDocument:TypeDocument):
        rpta=nuevo_admin.createTypeDocument(typeDocument)  
        return rpta
## tabla sede 

@router.post('/sede',status_code=201)

async def createSede(sede:Sede):
        rpta=nuevo_admin.createSede(sede)  
        return rpta

@router.get('/sede',response_model=List[Sede])

async def getSedes():
        rpta=nuevo_admin.getSedes()  
        return rpta['resultado']


@router.get('/sede/{id_sede}',response_model=Sede)

async def getSede(id_sede):
        rpta=nuevo_admin.getSede(id_sede)  
        return rpta



##tabla capacidad


@router.post('/capacidad',status_code=201)

async def createCapacidad(capacidad:Capacidad):
        rpta=nuevo_admin.createCapacidad(capacidad)  
        return rpta

@router.get('/capacidad',response_model=List[Capacidad])

async def getCapacidades():
        rpta=nuevo_admin.getCapacidades()  
        return rpta['resultado']


@router.get('/capacidad/{id_capacidad}',response_model=Capacidad)

async def getCapacidad(id_capacidad):
        rpta=nuevo_admin.getCapacidad(id_capacidad)  
        return rpta



