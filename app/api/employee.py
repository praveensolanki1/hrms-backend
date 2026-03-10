from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database.postgres import get_db
from app.models.employee import Employee
from app.models.attendance import Attendance
from fastapi.responses import JSONResponse
from fastapi import status

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.post("/")
def create_employee(data: dict, db: Session = Depends(get_db)):
    emp = Employee(**data)
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

@router.get("/")
def list_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@router.get("/summary")
def employees_summary(db: Session = Depends(get_db)):
    data = db.query(Employee.department, func.count(Employee.id).label("employees")).group_by(Employee.department).all()
    return [{"department": d, "employees": e} for d, e in data]

@router.get("/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Employee not found"}
        )

    return employee

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Employee not found"}
        )

    db.query(Attendance).filter(Attendance.employee_id == employee_id).delete()
    db.delete(employee)
    db.commit()

    return {"message": "Employee deleted successfully"}


