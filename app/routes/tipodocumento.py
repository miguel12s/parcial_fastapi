from fastapi import APIRouter
from typing import List
from controllers.tipodocumento import *
from models.TypeDocument import TypeDocument
tipoDocumento=APIRouter()

nuevo_tipoDocumento=TipoDocumentoController()

@tipoDocumento.get('/tipoDocumento/{id_type_document}',response_model=TypeDocument)


async def getTypeDocument(id_type_document):
    rpta=nuevo_tipoDocumento.getTypeDocument( id_type_document)
    return rpta


@tipoDocumento.get('/tipoDocumento')

async def getTypesDocuments():
    rpta=nuevo_tipoDocumento.getTypesDocuments()
    return rpta



@tipoDocumento.post('/tipoDocumento',status_code=201)


async def createTypeDocument(typeDocument:TypeDocument):
        rpta=nuevo_tipoDocumento.createTypeDocument(typeDocument)  
        return rpta


