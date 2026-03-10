from sqlalchemy import Column, Integer, Date, String, ForeignKey
from app.models.base_model import Base


class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    date = Column(Date)
    status = Column(String)