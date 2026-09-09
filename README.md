# FLOODWISE AI

### AI-Powered Urban Flood Nowcasting & Risk Intelligence System

> **See the flood before the street does.**

FLOODWISE AI is an AI-powered prototype for short-term urban flood risk prediction using rainfall, drainage capacity, elevation, previous water level, and drainage blockage conditions.

The system focuses on **0–3 hour flood nowcasting**, flood-risk classification, prototype water-depth estimation, drainage blockage simulation, safer-location identification, weather-data integration, and GIS-based visualization.

**Project Status:** Prototype / Active Development

---

## Overview

Urban flooding can develop rapidly due to intense rainfall, insufficient drainage capacity, drainage blockage, low-elevation areas, and accumulated surface water.

FLOODWISE AI aims to convert environmental and infrastructure-related information into an understandable short-term flood-risk signal that can support future urban flood monitoring and decision-support systems.

The current implementation is a **research and portfolio prototype**. It is not an operational flood-warning system.

---

## Key Capabilities

### Flood Risk Prediction

The system predicts:

* Flood probability
* Flood / No Flood classification
* Low / Medium / High risk level
* Prototype estimated water depth

### 0–3 Hour Nowcasting

The system evaluates flood risk for:

* Current conditions
* +1 hour
* +2 hours
* +3 hours

Each forecast step provides rainfall, predicted flood probability, risk classification, and estimated water depth.

### Drainage Blockage Simulation

Users can modify drainage blockage conditions and observe how changes in drainage conditions affect the predicted flood risk.

### GIS-Based Visualization

The system is designed to visualize geographic flood-risk information using coordinates and interactive maps.

### Safer Location Identification

The prototype identifies locations with comparatively lower predicted flood probability and water depth.

> **Current limitation:** the prototype identifies safer geographic points rather than performing real road-network navigation.

### Explainable Environmental Factors

The model uses the following environmental and infrastructure-related features:

* Rainfall
* Drainage capacity
* Elevation
* Previous water level
* Drainage blockage

### Weather Data Integration

The prototype supports integration with hourly weather forecast data for rainfall-based short-term prediction.

---

## Machine Learning

The current prototype uses a **Random Forest Classifier** implemented with Scikit-learn.

### Input Features

| Feature              | Description                            |
| -------------------- | -------------------------------------- |
| Rainfall             | Rainfall intensity in mm               |
| Drainage Capacity    | Relative drainage capacity             |
| Elevation            | Ground elevation                       |
| Previous Water Level | Previously accumulated water level     |
| Drainage Blockage    | Estimated drainage blockage percentage |

### Model Outputs

```text
Flood Probability
Flood / No Flood
Risk Classification
Estimated Water Depth
```

### Model Architecture

```text
Environmental & Infrastructure Data
                |
                v
        Feature Preparation
                |
                v
        Random Forest Model
                |
                v
        Flood Risk Prediction
                |
        +-------+-------+
        |       |       |
        v       v       v
     Risk    Nowcast  Water Depth
   Analysis    0–3h    Estimation
        |       |       |
        +-------+-------+
                |
                v
        GIS / Dashboard Layer
```

---

## Dataset & Validation

The current training dataset is **synthetic/prototype data generated for development and demonstration purposes**.

Therefore:

* The current model is not a scientifically validated flood forecasting model.
* Reported model performance should not be interpreted as real-world forecasting accuracy.
* Prototype water-depth values are estimation outputs, not measured water levels.

Future model development requires validated real-world datasets including:

* Historical flood observations
* High-resolution rainfall measurements
* Digital Elevation Models
* Drainage-network information
* Water-level observations
* Land-use and surface characteristics
* Historical weather conditions

Hydrological and hydraulic validation will also be required before any operational deployment.

---

## System Workflow

```text
Weather / Environmental Data
            |
            v
      Data Processing
            |
            v
     Feature Engineering
            |
            v
      Machine Learning
            |
            v
      Flood Risk Engine
            |
      +-----+-----+------+
      |           |      |
      v           v      v
   Prediction   0–3h   Location
               Nowcast  Analysis
      |           |      |
      +-----------+------+
                  |
                  v
          Dashboard / GIS
                  |
                  v
        User / Authority
```

---

## Technology Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest
* Joblib

### Data & Visualization

* Matplotlib
* Folium
* Pandas

### Dashboard

* Gradio

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Weather Data

* Open-Meteo API

### Development & Collaboration

* Google Colab
* Git
* GitHub

---

## Project Structure

```text
FLOODWISE-AI/
│
├── backend/
│   └── backend_api.py
│
├── data/
│   ├── raw/
│   └── processed/
│       └── floodwise_dataset.csv
│
├── models/
│   └── floodwise_model.pkl
│
├── notebooks/
│   └── FLOODWISE_AI_Main.ipynb
│
├── frontend/
├── gis/
├── src/
├── docs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Prototype Workflow

```text
User / Weather Input
        |
        v
Rainfall + Drainage + Elevation
+ Previous Water + Blockage
        |
        v
Random Forest Classifier
        |
        v
Flood Probability
        |
        v
Risk Classification
        |
        +-------------------+
        |                   |
        v                   v
Water Depth          0–3 Hour Nowcast
        |                   |
        +---------+---------+
                  |
                  v
          Dashboard Output
```

---

## Prototype Features

The current prototype demonstrates:

* AI-based flood-risk prediction
* 0–3 hour flood nowcasting
* Prototype water-depth estimation
* Drainage blockage simulation
* Safer-location identification
* Interactive GIS visualization
* Weather-data integration
* Gradio dashboard
* FastAPI backend prototype

---

## Live Prototype

The current interactive prototype is available through a temporary Gradio deployment.

**Demo:** [Launch FLOODWISE AI Prototype](https://5a0bb3df11907f74dd.gradio.live)

> The current Gradio deployment is temporary. A permanent production web application is under development.

---

## Backend API

The project includes a FastAPI backend prototype.

### Health Check

```http
GET /
```

### Flood Prediction

```http
POST /predict
```

Example request:

```json
{
  "rainfall": 80,
  "drainage": 45,
  "elevation": 4,
  "previous_water": 1.0,
  "blockage": 60
}
```

Example response:

```json
{
  "flood_probability": 82.5,
  "prediction": "FLOOD",
  "risk": "HIGH RISK",
  "estimated_water_depth_m": 5.91
}
```

> Example values are illustrative and should not be interpreted as validated real-world measurements.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sdey19-cyber/FLOODWISE-AI.git
cd FLOODWISE-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Backend

From the project root:

```bash
uvicorn backend.backend_api:app --reload
```

The API will be available locally at:

```text
http://127.0.0.1:8000
```

FastAPI interactive documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Notebook

The main machine-learning development notebook is:

```text
notebooks/FLOODWISE_AI_Main.ipynb
```

The notebook contains the prototype data generation, model training, prediction logic, nowcasting workflow, and experimentation.

---

## Limitations

The current version has several important limitations:

1. Training data is synthetic.
2. Flood labels are prototype-generated rather than derived from verified flood observations.
3. Water-depth estimation is a prototype mathematical estimation.
4. Safer-location analysis does not yet perform real road-network routing.
5. Weather integration is not yet a fully operational real-time forecasting pipeline.
6. The current model has not undergone hydrological or hydraulic validation.
7. The current deployment is intended for demonstration and research purposes.

---

## Future Development

The long-term goal is to develop FLOODWISE AI into a real-world urban flood intelligence platform.

Planned improvements include:

* Real-time rainfall ingestion
* Validated historical flood datasets
* High-resolution GIS layers
* Digital Elevation Model integration
* Drainage-network modelling
* Hydrological and hydraulic modelling
* Real road-network safe-route navigation
* Flood-risk heatmaps
* Real-time alerts
* Explainable AI dashboard
* Bengali and English interface
* Mobile-responsive web application
* IoT water-level sensor integration
* Authority / emergency-response dashboard
* Production-grade cloud deployment
* Model monitoring and continuous validation

---

## Project Origin

FLOODWISE AI was initially developed around the **Smart India Hackathon problem statement SIH26085 – Urban Flood Nowcasting System (Drainage and Rainfall Coupling)**.

The project is currently being developed further as an **independent technical portfolio and research prototype**.

---

## Developer

**Suparna Dey**

B.Tech CSE — Cyber Security

Areas of interest:

* Artificial Intelligence & Machine Learning
* AI Engineering
* Data Science
* Cyber Security
* Intelligent Systems

---

## Vision

The long-term vision of FLOODWISE AI is to build an intelligent urban flood early-warning and decision-support platform that transforms environmental, infrastructure, and geographic data into understandable and actionable flood-risk intelligence.

---

## Disclaimer

FLOODWISE AI is currently a **prototype research and portfolio project**.

The current machine-learning model uses synthetic/prototype data and has not been validated for operational flood forecasting.

Predicted flood probability and water-depth values must **not** be used as an emergency decision-making system.

Real-world deployment would require validated datasets, calibrated hydrological and hydraulic models, reliable weather and sensor feeds, extensive testing, and domain-expert validation.

---

## Project Status

**Prototype / Active Development**

The core machine-learning prototype, dashboard, backend API, weather integration, and GitHub project structure are currently implemented. Further development is focused on real-world data integration, GIS intelligence, explainability, routing, and production web deployment.
