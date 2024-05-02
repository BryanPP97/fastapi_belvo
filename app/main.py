from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.core.config import engine, Base
from app.api.linkid_endpoint import router as linkid_router 
from app.api.transactions_endpoint import router as transaction_router 
from app.api.auth import router as auth_router  
from app.api.users_endpoint import router as users_router
from app.service.financial_health_service import router as financial_health_router
from app.service.transactions_summary_service import router as transactions_summary_router
from app.service.accounts_financial_summary_service import router as accounts_financial_summary_router

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(auth_router)
app.include_router(linkid_router)
app.include_router(users_router)
app.include_router(transaction_router)
app.include_router(financial_health_router)
app.include_router(transactions_summary_router)
app.include_router(accounts_financial_summary_router)


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
