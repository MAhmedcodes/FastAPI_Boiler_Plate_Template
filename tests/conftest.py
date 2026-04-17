import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database.database import Base
from app.core.dependencies.dependencies import get_db
from main import app

# Use Docker service name, not localhost
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@postgres:5432/fastapi_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_default_organization():
    """Create default organization in test database"""
    from sqlalchemy import text
    with engine.connect() as conn:
        conn.execute(text(
            "INSERT INTO organizations (name, invite_token) VALUES ('default', 'default') ON CONFLICT (name) DO NOTHING"
        ))
        conn.commit()


@pytest.fixture(scope="function")
def db_session():
    # Create all tables in test database
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()

    # Cleanup after test
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


@pytest.fixture
def auth_token(client):
    # Create org
    org_response = client.post(
        "/organizations/create", json={"name": "Test Org"})
    if org_response.status_code != 200:
        pytest.skip(f"Failed to create org: {org_response.text}")

    org_data = org_response.json()
    invite_token = org_data["invite_token"]
    org_id = org_data["id"]

    # Register user
    register_response = client.post("/users/register", json={
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "test123",
        "invite_token": invite_token
    })
    if register_response.status_code != 200:
        pytest.skip(f"Failed to register: {register_response.text}")

    # Login
    response = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "test123",
        "organization_id": org_id
    })
    if response.status_code != 200:
        pytest.skip(f"Failed to login: {response.text}")

    return response.json()["access_token"]
