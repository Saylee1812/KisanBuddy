import os
import joblib
from fastapi import APIRouter, HTTPException, Query
from pymongo import MongoClient
import requests
import datetime
import numpy as np

router = APIRouter()

# === Load Model ===
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'rainfall_model.pkl')
model = joblib.load(model_path)

# === MongoDB Setup ===
client = MongoClient("mongodb://localhost:27017")
db = client["agrisens"]
rainfall_logs = db["rainfall_predictions"]

# === Weather API Key ===
API_KEY = "17e9f1dd50db4efd8bd91144253006"

# === Fetch Weather ===
def get_weather_data(city=None, lat=None, lon=None):
    if city:
        query = city
    elif lat is not None and lon is not None:
        query = f"{lat},{lon}"
    else:
        raise HTTPException(status_code=400, detail="Please provide either a city or latitude & longitude.")

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={query}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "current" not in data:
        raise HTTPException(status_code=400, detail=data.get("error", {}).get("message", "Failed to fetch weather"))

    location = data.get("location", {}).get("name", "Unknown Location")

    return {
        "location": location,
        "temperature": data["current"].get("temp_c", 0.0),
        "humidity": data["current"].get("humidity", 0.0),
        "pressure": data["current"].get("pressure_mb", 0.0),
        "windspeed": data["current"].get("wind_kph", 0.0),
        "rainfall_today": data["current"].get("precip_mm", 0.0)
    }

# === Irrigation Advice ===
def recommend_irrigation(will_rain, humidity, temperature):
    if will_rain:
        return "No irrigation needed — rain is expected tomorrow. ☔"
    if humidity < 30 and temperature > 35:
        return "Heavy irrigation recommended — dry and hot. 🔥"
    elif humidity < 50 and temperature > 30:
        return "Moderate irrigation recommended — warm and semi-dry. 🌤️"
    else:
        return "Light irrigation recommended. 🌱"

# === API Endpoint ===
@router.get("/predict_rainfall")
def rainfall_prediction(
    city: str = Query(None, description="City name (optional)"),
    lat: float = Query(None, description="Latitude (optional)"),
    lon: float = Query(None, description="Longitude (optional)")
):
    try:
        weather = get_weather_data(city=city, lat=lat, lon=lon)

        features = np.array([[   
            float(weather["pressure"]),
            float(weather["temperature"]),
            float(weather["humidity"]),
            float(weather["windspeed"]),
            float(weather["rainfall_today"]),
        ]])

        prediction = bool(model.predict(features)[0])
        irrigation = recommend_irrigation(prediction, weather["humidity"], weather["temperature"])

        rainfall_logs.insert_one({
            "timestamp": datetime.datetime.now(),
            "location": weather["location"],
            "lat": lat,
            "lon": lon,
            "city": city,
            "weather": {k: float(v) if isinstance(v, (int, float)) else v for k, v in weather.items()},
            "will_rain_tomorrow": prediction,
            "irrigation_advice": irrigation,
        })

        return {
            "location": weather["location"],
            "will_rain_tomorrow": prediction,
            "irrigation_advice": irrigation,
            "weather": weather,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
