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

## API Versioning and Routing:

- use `APIRouter()` from fastapi for this always
- create isolated routes within `/api/v$/{route}`
  - treat these as isolated routes, do not include the full `/api/v1/get-users` here (for complete separation without dependencies on route string)
  - add prefixes to these isolated routes in `/app/api/v$/api.py`, use this api in `main.py`
- in `app/main.py`, include all routers via `app.include_router(api_router, prefix="/api/v1")`

### Examples:

`/api/v1/users.py`:

```python
from fastapi import APIRouter, HTTPException

# Notice we don't put prefix="/users" here.
# We'll do that when we assemble the app.
router = APIRouter()

@router.get("/")
def get_all_users():
    return [{"id": 1, "username": "alice"}, {"id": 2, "username": "bob"}]

@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    if user_id not in [1, 2]:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, "username": "alice"}
```

`/api/v1/items.py`:

```python
from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_item(name: str):
    return {"name": name, "status": "created"}

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"id": item_id, "name": "Mechanical Keyboard"}
```

`/api/v1/api.py` (version aggregator):

```python
from fastapi import APIRouter
from app.api.v1 import users, items

api_router = APIRouter()

# Here is where we define the prefixes and tags for the OpenAPI docs
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(items.router, prefix="/items", tags=["Items"])
```

`main.py`:

```python
from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(
    title="My Large Project API",
    description="A cleanly structured FastAPI application.",
    version="1.0.0"
)

# Attach the entire v1 API under the /api/v1 prefix
app.include_router(api_router, prefix="/api/v1")

# This also allows you to attach another route that's v2 (js name router like api_router_v2)
# so, two versions will live side by side without impacting each other

@app.get("/health", tags=["System"])
def health_check():
    """Root-level endpoint for load balancers or uptime monitoring."""
    return {"status": "ok"}
```

## Pydantic as a Validator:

Refer to [pydantic.md](pydantic.md)

## Configuration and Secret Management with Pydantic:
