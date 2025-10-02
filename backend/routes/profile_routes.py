from fastapi import APIRouter, HTTPException, Depends
from database.connection import user_collection
from schemas.user_schema import user_serializer
from bson import ObjectId
from fastapi import Body
from utils.gemini import get_soil_recommendations

router = APIRouter(prefix="/profile")  # ✅ Add this prefix

@router.get("/user/{user_id}")
async def get_user(user_id: str):
    user = user_collection.find_one({"_id": ObjectId(user_id)})  # ✅ No await
    if user:
        return user_serializer(user)
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/user/{user_id}")
async def update_user(user_id: str, updated_data: dict = Body(...)):
    print("Received update for user:", user_id)
    print("Payload:", updated_data)

    result = user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": updated_data}
    )
    print("Matched count:", result.matched_count)
    print("Modified count:", result.modified_count)

    if result.modified_count:
        updated_user = user_collection.find_one({"_id": ObjectId(user_id)})
        return user_serializer(updated_user)

    raise HTTPException(status_code=404, detail="Update failed")

@router.get("/user/{user_id}/recommendations")
async def get_soil_suggestions(user_id: str):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    soil_data = {
        "pH": user.get("ph"),
        "nitrogen": user.get("nitrogen"),
        "phosphorus": user.get("phosphorus"),
        "potassium": user.get("potassium"),
        "moisture": user.get("moisture"),
        "soil_type": user.get("soil_type"),
        "irrigation_method": user.get("irrigation_method"),
    }

    fertility_result = user.get("soil_fertility_result", "Unknown")

    recommendations = get_soil_recommendations(soil_data, fertility_result)
    return {
        "user_id": str(user["_id"]),
        "fertility_result": fertility_result,
        "recommendations": recommendations
    }


