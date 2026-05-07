from fastapi import APIRouter

router = APIRouter(prefix="/users")

fake_users = []

@router.get("/")
async def list_users():
    return fake_users

@router.post("/")
async def create_user(user: dict):
    fake_users.append(user)
    return user
