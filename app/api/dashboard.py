from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.postgres import get_db
from app.models.employee import Employee
from app.models.attendance import Attendance

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard(db: Session = Depends(get_db)):

    total_employees = db.query(Employee).count()
    total_attendance = db.query(Attendance).count()

    return {
        "total_employees": total_employees,
        "attendance_records": total_attendance
    }