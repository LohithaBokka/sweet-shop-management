# Sweet Shop Management System

A full-stack web application to manage sweets inventory, user authentication,
and basic shop operations using a RESTful API and frontend interface.

---

## Tech Stack

### Backend
- FastAPI (Python)
- SQLite
- SQLAlchemy
- JWT Authentication

### Frontend
- React
- Axios
- CSS

### Testing
- Pytest

### Version Control
- Git & GitHub

---

## How to Run the Project Locally

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # For Windows
# source venv/bin/activate   # For Mac/Linux
pip install -r requirements.txt
uvicorn app.main:app --reload
