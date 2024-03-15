from fastapi import APIRouter, Depends
from schemas import User, UserBase


users_router = APIRouter(prefix="/users", tags=["users"])

users = [{"nombre": "johan", "passwprd": "1234"}, {"nombre": "johan", "passwprd": "1234"}]

@users_router.get("/")
async def read_users():
    return users

@users_router.post("/")
async def create_user(new_user: User) -> UserBase:
    users.append(new_user)
    
    return new_user

@users_router.get("/{user_id}")
async def read_user(user_id: int,q: str = None):
    return {"user_id": user_id, "q": q}