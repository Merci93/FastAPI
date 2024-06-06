import pytest

from fastapi.testclient import TestClient

from src import main


@pytest.fixture
def test_client() -> TestClient:
    """
    Returns a testclient used for testing the FastAPI endpoints.
    """
    return TestClient(main.app)
