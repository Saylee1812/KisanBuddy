from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from bson.errors import InvalidId  # ✅ Needed to catch bad ObjectIds
from services.soil_analysis import predict_soil_fertility
from database.connection import user_collection

router = APIRouter()

class SoilFertilityInput(BaseModel):
    N: float
    P: float
    K: float
    pH: float
    EC: float
    OC: float
    S: float
    Zn: float
    Fe: float
    Cu: float
    Mn: float
    B: float
    user_id: str

@router.post("/analyze")
def analyze_soil(data: SoilFertilityInput):
    data_dict = data.dict()
    user_id = data_dict.pop("user_id")

    # ✅ Handle invalid ObjectId
    try:
        object_id = ObjectId(user_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user_id format")

    # Predict soil fertility
    fertility_result = predict_soil_fertility(data_dict)

    # Save to MongoDB
    result = user_collection.update_one(
        {"_id": object_id},
        {"$set": {
            "soil_fertility_result": fertility_result,
            **data_dict
        }}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user_id": user_id,
        "fertility_result": fertility_result,
        "message": "Fertility result saved successfully"
    }
