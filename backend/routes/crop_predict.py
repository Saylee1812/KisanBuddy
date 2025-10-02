from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os, pickle, numpy as np
from database.connection import db

model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'RF.pkl')
model = pickle.load(open(model_path, 'rb'))

router = APIRouter()
crop_info_collection = db["crop_info"]

class CropInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@router.post("/predict_crop")
def predict_crop(data: CropInput):
    try:
        features = np.array([[data.N, data.P, data.K, data.temperature, data.humidity, data.ph, data.rainfall]])
        predicted_crop = model.predict(features)[0]

        # ⬇️ Fetch extra info from DB
        info = crop_info_collection.find_one({"crop": predicted_crop})
        if info:
            return {
                "prediction": predicted_crop,
                "reason": info.get("reason"),
                "sowing_period": info.get("sowing_period"),
                "tip": info.get("tip")
            }
        else:
            return {"prediction": predicted_crop, "message": "No extra info found in DB."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
