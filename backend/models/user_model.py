from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    username: str
    email: str
    password: str
    phone: Optional[str] = None
    location: Optional[str] = None
    farming_type: Optional[str] = None
    crops: Optional[List[str]] = []
    land_size: Optional[str] = None
    soil_type: Optional[str] = None
    irrigation_method: Optional[str] = None
    preferred_language: Optional[str] = None
    experience: Optional[str] = None
    weather_alerts: Optional[bool] = False

class UserLogin(BaseModel):
    email: str
    password: str
