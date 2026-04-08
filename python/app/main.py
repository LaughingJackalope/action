from fastapi import FastAPI
from .routers import users

app = FastAPI(
    title="User Management API",
    version="1.0.0",
    description="A mock service for CI/CD workflow testing",
)

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Mock User Management API"}
