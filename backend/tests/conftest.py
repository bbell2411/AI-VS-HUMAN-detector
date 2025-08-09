import pytest
from app.main import app
from fastapi.testclient import TestClient
from app.database import Base, engine

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True, scope="function")
def setup_test_database():
    """Create fresh database tables for each test."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    
    
    