from fastapi import FastAPI
from app.database.database import engine
from app.models.user import User

app = FastAPI(title="Sweet Shop Management System")

# Create DB tables
User.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Sweet Shop API is running"}
