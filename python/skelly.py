from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="User Management API", version="1.0.0")


# --- THE CONTRACT (Data Model) ---
class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: Optional[bool] = True


# --- THE INTERFACE (Routes) ---

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    """
    Retrieve a user by their ID.
    The response_model ensures the output matches our contract.
    """
    # Mock Database Logic
    if user_id == 42:
        return {
            "id": 42,
            "username": "fastapi_dev",
            "email": "py@example.com"
        }

    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users/", response_model=User, status_code=201)
async def create_user(user: User):
    """
    Endpoint to create a user.
    FastAPI automatically validates the incoming JSON against the User model.
    """
    return user