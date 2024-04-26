from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.core.config import engine, Base
from app.api.endpoints import router  # Mueve la importación aquí para evitar duplicados

app = FastAPI()

app.include_router(router)  # Asegúrate de que esto solo aparezca una vez

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)  # Inicialización de la base de datos

@app.exception_handler(Exception)
def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred", "details": str(exc)},
    )
