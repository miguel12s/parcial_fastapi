from fastapi import FastAPI
from routes.campoad import campoad
from routes.capacidad import capacidad
from routes.facultad import facultad
from routes.materia import materia
from routes.programa import programa
from routes.programaxfacultad import programaxfacultad
from routes.rol import rol
from routes.sede import sede
from routes.tipodocumento import tipoDocumento
from routes.tipoestado import tipoEstado
from routes.tiporegistro import tipoRegistro
from routes.tipoxestado import tipoxestado
from routes.user_routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    # "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(campoad)
app.include_router(capacidad)
app.include_router(facultad)
app.include_router(materia)
app.include_router(programa)
app.include_router(programaxfacultad)
app.include_router(rol)
app.include_router(sede)
app.include_router(tipoDocumento)
app.include_router(tipoEstado)
app.include_router(tipoRegistro)
app.include_router(tipoxestado)
app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)