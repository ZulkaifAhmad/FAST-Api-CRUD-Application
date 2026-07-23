from fastapi import APIRouter
from app.services.user_services import UserService
from app.schemas.user_schema import User

router = APIRouter(tags=["users"])
services = UserService()

@router.get("/")
def Home_Route():
    msg = services.home()
    return {
        "message": msg,
        "success": True
    }

@router.get("/users")
def All_Users():
    users = services.get_all_users()
    return {
        "message": "Users Fetched Successfully",
        "success": True,
        "users": users
    }

@router.get("/user/{user_id}")
def User_byID(user_id: int):
    user = services.get_specific_user(user_id)
    return {
        "message": "User fetched Successfully",
        "success": True,
        "user": user
    }

@router.post("/user")
def Create_User(user: User):
    created = services.create_user(user)
    return {
        "message": "User created Successfully",
        "success": True,
        "user": created
    }

@router.put("/user/{user_id}")
def Update_User(user_id: int, updated_user: User):
    updated = services.update_specific_user(user_id, updated_user)
    return {
        "message": "User updated Successfully",
        "success": True,
        "user": updated
    }

@router.delete("/user/{user_id}")
def Delete_User(user_id: int):
    deleted = services.delete_user(user_id)
    return {
        "message": "User deleted Successfully",
        "success": True,
        "user": deleted
    }