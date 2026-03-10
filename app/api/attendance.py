from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date
from app.database.postgres import get_db
from app.models.employee import Employee
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate
from sqlalchemy import func
from fastapi.responses import JSONResponse
from fastapi import status

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/")
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):

    employee = db.query(Employee).filter(
        Employee.id == data.employee_id
    ).first()

    if not employee:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Employee not found"}
        )


    attendance = Attendance(
        employee_id=data.employee_id,
        date=data.date,
        status=data.status
    )

    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return attendance


@router.get("/summary")
def attendance_summary(db: Session = Depends(get_db)):
    data = db.query(Employee.name, func.count(Attendance.id).label("attendance_count")).join(Attendance, Employee.id == Attendance.employee_id).group_by(Employee.name).all()
    return [{"employee": name, "attendance_count": count} for name, count in data]

@router.get("/{employee_id}")
def employee_attendance(employee_id: int, db: Session = Depends(get_db)):

    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()



