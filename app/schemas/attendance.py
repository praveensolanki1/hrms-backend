from pydantic import BaseModel
from datetime import date
from app.models.enums import AttendanceStatus


class AttendanceCreate(BaseModel):
    employee_id: int
    date: date
    status: AttendanceStatus


class AttendanceResponse(BaseModel):
    id: int
    employee_id: int
    date: date
    status: AttendanceStatus

    class Config:
        from_attributes = True