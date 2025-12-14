from fastapi import FastAPI
from app.database.database import engine
from app.models.user import User
from app.routers import auth, sweets

app = FastAPI(title="Sweet Shop Management System")

# Create DB tables
User.metadata.create_all(bind=engine)

# Include router
app.include_router(auth.router)
app.include_router(sweets.router)

@app.get("/")
def root():
    return {"message": "Sweet Shop API is running"}
