import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.database.database import Base
from app.core.dependencies.dependencies import get_db
from app.main import app

# Docker service name (IMPORTANT)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@postgres:5432/fastapi_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# -------------------------
# DATABASE LIFECYCLE
# -------------------------
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()

    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


# -------------------------
# FASTAPI CLIENT (OVERRIDE DB)
# -------------------------
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()


# -------------------------
# AUTH FIXTURE (SAFE UNIQUE DATA)
# -------------------------
@pytest.fixture
def auth_token(client):
    import uuid

    email = f"user_{uuid.uuid4()}@test.com"
    org_name = f"org_{uuid.uuid4()}"

    org = client.post("/organizations/create", json={"name": org_name})
    assert org.status_code == 200
    org_data = org.json()

    register = client.post("/users/register", json={
        "email": email,
        "first_name": "Test",
        "last_name": "User",
        "password": "test123",
        "invite_token": org_data["invite_token"]
    })
    assert register.status_code == 200

    login = client.post("/auth/login", data={
        "username": email,
        "password": "test123",
        "organization_id": org_data["id"]
    })
    assert login.status_code == 200

    return login.json()["access_token"]
