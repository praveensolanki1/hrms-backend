from fastapi import FastAPI

from app.database.postgres import engine
from app.models.base_model import Base

from app.api.employee import router as employee_router
from app.api.attendance import router as attendance_router
from app.api.dashboard import router as dashboard_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HRMS Backend")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(employee_router)
app.include_router(attendance_router)
app.include_router(dashboard_router)

@app.get("/")
def health():
    return {"message": "HRMS backend running"}