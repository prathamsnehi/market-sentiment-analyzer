## Directory Structure:

```md
my_fastapi_project/
├── alembic/ # Database migrations
├── app/ # Main application code
│ ├── api/ # API Routers (Controllers)
│ │ ├── dependencies/ # Shared dependencies (e.g., get_db, get_current_user)
│ │ └── v1/ # Versioned API routes
│ │ ├── users.py
│ │ └── items.py
│ ├── core/ # App-wide settings and configs
│ │ ├── config.py # Pydantic BaseSettings
│ │ └── security.py # Hashing, JWT tokens
│ ├── crud/ # Database interactions (Repository layer)
│ ├── models/ # Database models (e.g., SQLAlchemy)
│ ├── schemas/ # Pydantic models (Data validation)
│ ├── services/ # Business logic (Optional but recommended)
│ ├── db/ # Database setup and sessions
│ └── main.py # FastAPI application instance
├── tests/ # Pytest directory
├── .env # Environment variables
├── alembic.ini # Alembic configuration
└── requirements.txt # or pyproject.toml / poetry.lock
```

Explanation of each of the components in the directory structure above:

- Routers (`app/api/*`):
  - as dumb as possible
  - their only job is to receive the HTTP request, pass it to a CRUD / controller function, and return response
- Services / Business Logic (`app/services/*`):
  - eg: generating an AI response, checking if user has hit limits, etc etc
- CRUD (`app/crud/*`):
  - handles raw database operations
  - should only be used for database ops

## Server Assembly (`app/main.py`):
