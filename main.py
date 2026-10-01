from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI(
    title="Dietitian & Nutrition Management System",
    version="2.0.0",
    description="REST API for the Dietitian & Nutrition Management System"
)


# =========================
# Health Check
# =========================

@app.get("/")
def read_root():
    return {
        "message": "Dietitian & Nutrition Management System API",
        "version": "2.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# =========================
# Appointment Models
# =========================

class AppointmentCreate(BaseModel):
    client_id: str
    dietitian_id: str
    appointment_date: str
    reason: Optional[str] = None


# Temporary appointment storage
appointments = []


# =========================
# Appointments
# =========================

@app.get("/appointments")
def list_appointments():
    return {
        "appointments": appointments
    }


@app.post("/appointments")
def create_appointment(appointment: AppointmentCreate):
    new_appointment = {
        "appointment_id": f"APT{len(appointments) + 1:03d}",
        "client_id": appointment.client_id,
        "dietitian_id": appointment.dietitian_id,
        "appointment_date": appointment.appointment_date,
        "reason": appointment.reason,
        "status": "PENDING"
    }

    appointments.append(new_appointment)

    return {
        "message": "Appointment created successfully",
        "appointment": new_appointment
    }


# =========================
# Goal Model
# =========================

class GoalCreate(BaseModel):
    client_id: str
    goal_type: str
    description: str
    target_value: Optional[str] = None


# Temporary goal storage
goals = []


# =========================
# Goals
# =========================

@app.post("/goals")
def create_goal(goal: GoalCreate):
    new_goal = {
        "goal_id": f"GOAL{len(goals) + 1:03d}",
        "client_id": goal.client_id,
        "goal_type": goal.goal_type,
        "description": goal.description,
        "target_value": goal.target_value,
        "status": "ACTIVE"
    }

    goals.append(new_goal)

    return {
        "message": "Goal created successfully",
        "goal": new_goal
    }