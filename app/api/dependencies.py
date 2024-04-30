from app.core.config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db #Asegura que la sesión solo se mantenga abierta durante el tiempo necesario para procesar la solicitud.
    finally:
        db.close()
