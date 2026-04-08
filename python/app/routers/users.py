from fastapi import APIRouter, HTTPException
from ..models import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    """
    Retrieve a user by their ID.
    """
    # Mock Database Logic
    if user_id == 42:
        return {
            "id": 42,
            "username": "fastapi_dev",
            "email": "py@example.com"
        }

    raise HTTPException(status_code=404, detail="User not found")

@router.post("/", response_model=User, status_code=201)
async def create_user(user: User):
    """
    Endpoint to create a user.
    """
    return user
