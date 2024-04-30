from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.core.config import engine, Base
from app.api.endpoints import router as api_router 
from app.api.auth import router as auth_router  
from app.api.users import router as users_router    
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(api_router)
app.include_router(auth_router)
app.include_router(users_router)

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)  # Inicialización de la base de datos

# Función como manejador de excepciones para todas las excepciones no capturadas explícitamente
@app.exception_handler(Exception)
def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred", "details": str(exc)},
    )
