from fastapi.testclient import TestClient
from pytest import fixture
from app.main import app
from app.api.dependencies import get_db
from sqlalchemy.orm import Session

# Fixture para el cliente de test
@fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

# Fixture para obtener la sesión de base de datos, utilizando la configuración actual de la app
@fixture(scope="function")
def db_session():
    session = next(get_db())  # Suponiendo que `get_db` yield una sesión de SQLAlchemy
    try:
        yield session
    finally:
        session.rollback()

# Test para registrar un usuario
def test_register_user(client, db_session):
    app.dependency_overrides[get_db] = lambda: db_session
    response = client.post(
        "/register",
        json={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Usuario creado exitosamente"}