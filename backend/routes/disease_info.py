from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from fastapi.responses import JSONResponse

disease_info = APIRouter()

client = MongoClient("mongodb://localhost:27017")  # or your connection URI
db = client["AgriSens1"]  # Replace with your DB name
collection = db["disease_info"]  # Replace with your collection name

@disease_info.get("/plant-disease/info/{disease_id}")
async def get_disease_info(disease_id: str):
    disease = collection.find_one({"_id": disease_id})
    if not disease:
        raise HTTPException(status_code=404, detail="Disease not found")

    # Convert ObjectId if any
    disease["_id"] = str(disease["_id"])
    return JSONResponse(content=disease)
