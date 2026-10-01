from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_get_appointments():
    response = client.get("/appointments")
    assert response.status_code == 200


def test_create_appointment():
    appointment = {
        "client_id": "CLI001",
        "dietitian_id": "DT001",
        "appointment_date": "2026-10-05",
        "reason": "Initial nutrition consultation"
    }

    response = client.post("/appointments", json=appointment)

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Appointment created successfully"
    assert data["appointment"]["client_id"] == "CLI001"


def test_create_goal():
    goal = {
        "client_id": "CLI001",
        "goal_type": "Weight Management",
        "description": "Reach a healthy target weight",
        "target_value": "65 kg"
    }

    response = client.post("/goals", json=goal)

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Goal created successfully"
    assert data["goal"]["client_id"] == "CLI001"