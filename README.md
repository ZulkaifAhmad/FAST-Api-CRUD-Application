# FastAPI User CRUD API 🚀

My first ever FastAPI project — a simple CRUD (Create, Read, Update, Delete) API for managing users, built with a clean, industry-style folder structure.

This project uses in-memory storage (a Python list) instead of a real database, as a starting point to learn FastAPI fundamentals and proper project organization.

## Features

- Create a new user
- Get all users
- Get a single user by ID
- Update a user
- Delete a user
- Auto-generated interactive API docs (Swagger UI)

## Tech Stack

- **FastAPI** — Python web framework
- **Pydantic** — data validation
- **Uvicorn** — ASGI server

## Project Structure

```
fastapi-app/
│
├── app/
│   ├── main.py                 # App entrypoint
│   ├── schemas/
│   │   └── user_schema.py      # User data model
│   ├── routers/
│   │   └── user_router.py      # API routes
│   ├── services/
│   │   └── user_service.py     # Business logic
│   └── store/
│       └── user_store.py       # In-memory data storage
│
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd fastapi-app
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
uvicorn app.main:app --reload
```

The API will be running at:
```
http://127.0.0.1:8000
```

## API Documentation

Once the server is running, visit:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

| Method | Endpoint            | Description          |
|--------|----------------------|-----------------------|
| GET    | `/`                  | Welcome message       |
| GET    | `/users`             | Get all users         |
| GET    | `/user/{user_id}`    | Get a single user     |
| POST   | `/create-user`       | Create a new user     |
| PUT    | `/user/{user_id}`    | Update a user         |
| DELETE | `/user/{user_id}`    | Delete a user          |

## Example Request (Create User)

**POST** `/create-user`
```json
{
  "username": "zulkaif",
  "age": 22,
  "email": "zulkaif@example.com"
}
```

**Response**
```json
{
  "message": "User created Successfully",
  "success": true,
  "user": {
    "username": "zulkaif",
    "age": 22,
    "email": "zulkaif@example.com"
  }
}
```

## Note

This project currently uses **in-memory storage**, meaning data resets every time the server restarts. A real database (MongoDB) integration is planned as a next step.

## Author

**Zulkaif Ahmad**
MERN Stack / Next.js Developer, learning backend development with FastAPI
GitHub: [ZulkaifAhmad](https://github.com/ZulkaifAhmad)