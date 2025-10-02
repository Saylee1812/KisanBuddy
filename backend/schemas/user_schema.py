#schemas/user_shema.py
def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user.get("username"),
        "email": user.get("email"),
        "phone": user.get("phone"),
        "location": user.get("location"),
        "farming_type": user.get("farming_type"),
        "crops": user.get("crops", []),
        "land_size": user.get("land_size"),
        "soil_type": user.get("soil_type"),
        "irrigation_method": user.get("irrigation_method"),
        "preferred_language": user.get("preferred_language"),
        "experience": user.get("experience"),
        "weather_alerts": user.get("weather_alerts", False)
    }
