from app import main
from app.main import FastAPI


def test_ping(test_app: FastAPI):
    # Given
    # test_app

    # When
    response = test_app.get("/ping")

    # Then
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!", "environment": "dev", "testing": True}
