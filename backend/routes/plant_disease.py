from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

plant_disease = APIRouter()

MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models", "trained_plant_disease_model.keras"))
model = tf.keras.models.load_model(MODEL_PATH)

class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
    'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
    'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy']

@plant_disease.post("/plant-disease/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).resize((128, 128))
    image_array = np.array(image)

    if image_array.shape[-1] != 3:
        image_array = np.stack([image_array]*3, axis=-1)

    input_array = np.expand_dims(image_array, axis=0)
    prediction = model.predict(input_array)
    predicted_class = class_names[np.argmax(prediction)]

    return JSONResponse(content={"result": predicted_class})
