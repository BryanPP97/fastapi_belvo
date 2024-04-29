import os
from dotenv import load_dotenv
from belvo.client import Client
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno
load_dotenv()

def get_belvo_client():
    return Client(
        os.getenv("BELVO_SECRET_KEY_ID"),
        os.getenv("BELVO_SECRET_KEY"),
        "sandbox"
    )


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Clave secreta para firmar tokens JWT
SECRET_KEY = os.getenv("SECRET_KEY")
