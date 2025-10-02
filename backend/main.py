from fastapi import FastAPI
from routes.auth_routes import auth
from routes.chat import router as chat
from routes.profile_routes import router
from routes.plant_disease import plant_disease
from routes.soil import router as soil_router
from routes.crop_predict import router as crop_router
from routes.rainfall import router as rainfall_router
from routes.disease_info import disease_info 

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)
app.include_router(chat)
app.include_router(router)
app.include_router(plant_disease)
app.include_router(rainfall_router, prefix="/rainfall", tags=["Rainfall Prediction"])
app.include_router(soil_router, prefix="/soil", tags=["Soil Analysis"])
app.include_router(crop_router, prefix="/crop", tags=["Crop Prediction"])
app.include_router(disease_info)

@app.get("/")
def read_root():
    return {"message": "Welcome to KisanBuddy Backend API!"}