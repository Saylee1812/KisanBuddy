from fastapi import APIRouter, Request, HTTPException, Depends
from bson import ObjectId
from fastapi.concurrency import run_in_threadpool
from database.connection import user_collection
from utils.gemini import generate_gemini_response  # your Gemini wrapper

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_id = body.get("user_id")
    message = body.get("message")

    if not user_id or not message:
        raise HTTPException(status_code=400, detail="user_id and message required")

    # Step 1: Get user profile from DB
    user = await run_in_threadpool(lambda: user_collection.find_one({"_id": ObjectId(user_id)}))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Step 2: Format prompt with user data
    user_context = f"""
    You are assisting a farmer. Here is their profile:
    - Name: {user.get('username')}
    - Location: {user.get('location')}
    - Farming Type: {user.get('farming_type')}
    - Crops: {', '.join(user.get('crops', []))}
    - Land Size: {user.get('land_size')}
    - Soil Type: {user.get('soil_type')}
    - Irrigation Method: {user.get('irrigation_method')}
    - Experience: {user.get('experience')}
    - Preferred Language: {user.get('preferred_language')}
    - Weather Alerts: {"enabled" if user.get('weather_alerts') else "disabled"}

    Based on this, answer the user's question below.
    Question: {message}
    """

    # Step 3: Get Gemini response
    reply = await generate_gemini_response(user_context)

    # Step 4: Return response
    return {"response": reply}
