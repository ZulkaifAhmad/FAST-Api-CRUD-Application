from fastapi import HTTPException
from app.schemas.user_schema import User 
from app.store.user_store import list

class UserService:
    def home(self):
        # return a simple message string; router will wrap it in a response dict
        return "Welcome Home! , Hello world to Fast Api"
    
    def get_all_users(self):
        # return raw list of users; router will wrap it
        return list
        
    def get_specific_user(self, user_id: int):
        if user_id < 0 or user_id >= len(list):
            raise HTTPException(status_code=404, detail="User not found")
        # return the user object directly
        return list[user_id]
    
    def create_user(self, user: User):
        list.append(user)
        # return the created user object
        return user
    
    def update_specific_user(self, user_id: int, updated_user: User):
        if user_id < 0 or user_id >= len(list):
            raise HTTPException(status_code=404, detail="User not found")

        list[user_id] = updated_user
        # return the updated user object
        return updated_user
    
    def delete_user(self, user_id: int):
        if user_id < 0 or user_id >= len(list):
            raise HTTPException(status_code=404, detail="User not found")
        deleted_user = list[user_id]
        del list[user_id]
        # return the deleted user object
        return deleted_user
