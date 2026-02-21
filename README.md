# fast_api_app

📘 fast_api_app
A simple FastAPI-based REST API for managing a list of students — with standard CRUD (Create, Read, Update, Delete) endpoints.

This project lets you quickly spin up an API to add, list, get, update, and delete student records using FastAPI. It’s minimal but practical as a starter or learning reference.

🚀 Features
✔ Basic student CRUD endpoints
✔ Uses Pydantic models for request validation
✔ Built with FastAPI — auto-generated API docs included
✔ Easy to run locally

📦 Tech Stack
Technology	Purpose
FastAPI	API framework
Pydantic	Data validation
Uvicorn	ASGI server
SQLAlchemy (listed, not yet used)	DB models / migrations (future)
Dependencies listed in requirements.txt:

Fastapi
sqlalchemy
uvicorn[standard]
pydantic

📍 Endpoints
✔ GET /
Returns a greeting JSON.

✔ GET /students
List all students.

✔ POST /students
Create a new student — requires JSON body.

✔ GET /students/{roll}
Retrieve student by roll number.

✔ PUT /students/{roll}
Update an existing student.

✔ DELETE /students/{roll}
Remove student from list.

All request/response models are documented automatically by FastAPI. 

🏁 Quick Start (Local)
1) Clone
git clone https://github.com/prithvihn/fast_api_app.git
cd fast_api_app
2) Create Virtual Environment (strongly recommended)
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
3) Install Dependencies
pip install -r requirements.txt
4) Run the API
uvicorn main:app --reload
The API runs at: http://127.0.0.1:8000

Open interactive docs at: http://127.0.0.1:8000/docs

🧠 Example Student JSON (POST /students)
{
  "name": "Alice",
  "email": "alice@example.com",
  "age": 22,
  "Roll_number": "R123",
  "Department": "CS"
}
⚙️ Notes / Things to Fix
Your main.py has duplicate @app.get("/") and missing response models on some endpoints — bugs will occur if you hit the root route twice.

sqlalchemy is listed in requirements but not used in code — remove or actually integrate it.

Deletion logic currently references a missing student variable.

I can help rewrite/fix the backend logic too if you want that. 👌

📌 Want Better API Design?
If you want to structure this as a real project with:

✔ Database persistence (SQLite / PostgreSQL)
✔ Auth (JWT / OAuth)
✔ Pagination / filtering
✔ Versioned routes
✔ Unit tests
