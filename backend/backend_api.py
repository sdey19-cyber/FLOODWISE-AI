
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="FLOODWISE AI API")

model = joblib.load("floodwise_model.pkl")


class FloodInput(BaseModel):
    rainfall: float
    drainage: float
    elevation: float
    previous_water: float
    blockage: float


@app.get("/")
def home():
    return {
        "message": "FLOODWISE AI Backend is running!"
    }


@app.post("/predict")
def predict_flood(data: FloodInput):

    new_data = pd.DataFrame({
        "rainfall_mm": [data.rainfall],
        "drainage_capacity": [data.drainage],
        "elevation_m": [data.elevation],
        "previous_water_level_m": [data.previous_water],
        "drainage_blockage_percent": [data.blockage]
    })

    probability = model.predict_proba(new_data)[0][1] * 100
    prediction = model.predict(new_data)[0]

    if probability >= 75:
        risk = "HIGH RISK"
    elif probability >= 40:
        risk = "MEDIUM RISK"
    else:
        risk = "LOW RISK"

    return {
        "flood_probability": round(probability, 2),
        "prediction": "FLOOD" if prediction == 1 else "NO FLOOD",
        "risk": risk
    }
