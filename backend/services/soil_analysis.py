# services/soil_analysis.py

import pickle
import numpy as np
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'soil_fertility_model.pkl')

# Load the model once
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

def predict_soil_fertility(data: dict):
    features = [
        data["N"], data["P"], data["K"], data["pH"], data["EC"], data["OC"],
        data["S"], data["Zn"], data["Fe"], data["Cu"], data["Mn"], data["B"]
    ]

    # Apply log transform (same as training)
    features_np = np.array(features).reshape(1, -1)
    prediction = model.predict(features_np)[0]

    label_map = {
        0: "Less Fertile",
        1: "Fertile",
        2: "Highly Fertile"
    }
    return label_map.get(prediction, "Unknown")
