
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI(title="FLOODWISE AI API")

# Load model from the project's models directory
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "floodwise_model.pkl"

model = joblib.load(MODEL_PATH)


class FloodInput(BaseModel):
    rainfall: float
    drainage: float
    elevation: float
    previous_water: float
    blockage: float


def estimate_water_depth(rainfall, drainage, elevation):
    depth = (
        (rainfall * 0.08)
        - (drainage * 0.02)
        - (elevation * 0.03)
    )

    return round(max(depth, 0), 2)


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

    water_depth = estimate_water_depth(
        data.rainfall,
        data.drainage,
        data.elevation
    )

    return {
        "flood_probability": round(probability, 2),
        "prediction": "FLOOD" if prediction == 1 else "NO FLOOD",
        "risk": risk,
        "estimated_water_depth_m": water_depth
    }
