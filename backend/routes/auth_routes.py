from fastapi import APIRouter, HTTPException
from models.user_model import User, UserLogin
from database.connection import user_collection
from utils.auth import hash_password, verify_password, create_access_token
from schemas.user_schema import user_serializer

auth = APIRouter()

@auth.post("/signup")
def signup(user: User):
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pwd = hash_password(user.password)
    user_data = dict(user)
    user_data["password"] = hashed_pwd
    user_collection.insert_one(user_data)
    return {"message": "User created successfully"}

@auth.post("/login")
def login(user: UserLogin):
    db_user = user_collection.find_one({"email": user.email})
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect password")

    token = create_access_token({
        "email": db_user["email"],
        "user_id": str(db_user["_id"])  # ✅ include user_id in token (optional but good)
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": str(db_user["_id"])  # ✅ Add this so frontend can save it
    }
