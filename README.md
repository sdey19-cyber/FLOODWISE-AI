# 🌊 FLOODWISE AI

### AI-Powered Urban Flood Nowcasting & Risk Intelligence System

> **“See the flood before the street does.”**

FLOODWISE AI is an AI-powered prototype designed to predict short-term urban flood risk using rainfall, drainage capacity, elevation, previous water level, and drainage blockage information.

The system focuses on **0–3 hour flood nowcasting**, estimated water depth, risk classification, safer-location identification, drainage blockage simulation, and GIS-based visualization.

---

## 🚨 Problem

Urban flooding can develop rapidly because of:

- Intense rainfall
- Poor drainage capacity
- Drainage blockage
- Low-elevation areas
- Accumulated water from previous hours

Traditional flood monitoring may not provide sufficiently localized, short-term risk information for individual urban areas.

**FLOODWISE AI aims to provide an early, understandable risk signal before flooding becomes severe.**

---

## ✨ Key Features

### 🌧️ 1. Flood Risk Prediction

Predicts:

- Flood probability
- Flood / No Flood classification
- Low / Medium / High risk level
- Estimated water depth

### ⏱️ 2. 0–3 Hour Flood Nowcasting

Provides a short-term forecast for:

- Current conditions
- +1 hour
- +2 hours
- +3 hours

The dashboard displays predicted flood probability, risk level, rainfall and estimated water depth.

### 🕳️ 3. Drainage Blockage Simulation

Users can change drainage blockage conditions and observe how the predicted flood risk changes.

### 🗺️ 4. GIS-Based Flood Visualization

The system is designed to visualize flood-prone and safer areas using geographic coordinates and interactive maps.

### 📍 5. Safer Location Identification

The prototype identifies locations with comparatively lower predicted flood probability and water depth.

> Current prototype identifies safer points rather than performing real road-network navigation.

### 🤖 6. Explainable AI

Important environmental factors used by the model include:

- Rainfall
- Drainage capacity
- Elevation
- Previous water level
- Drainage blockage

### 🌦️ 7. Weather Data Integration

The prototype supports integration with hourly weather forecast data for short-term rainfall-based prediction.

---

## 🧠 Machine Learning

The current prototype uses a **Random Forest Classifier**.

### Input Features

```text
Rainfall
Drainage Capacity
Elevation
Previous Water Level
Drainage Blockage
Output
Flood Probability
Flood / No Flood
Risk Level
Estimated Water Depth

The current training dataset is synthetic/prototype data created for development and demonstration.

Therefore, the current model should not be interpreted as a scientifically validated real-world flood prediction model.

Future versions will require real historical flood observations, high-resolution rainfall data, drainage-network information, DEM/elevation data, and hydrological/hydraulic validation.

🏗️ System Architecture
Weather / Environmental Data
            ↓
      Data Processing
            ↓
     Feature Engineering
            ↓
      Machine Learning Model
            ↓
   ┌────────┼─────────┐
   ↓        ↓         ↓
Flood    0–3h      Safer
Risk    Nowcast    Locations
   ↓        ↓         ↓
   └────────┼─────────┘
            ↓
       GIS Dashboard
            ↓
      User / Authority
🛠️ Technology Stack
Machine Learning
Python
Pandas
NumPy
Scikit-learn
Random Forest
Data & Visualization
Matplotlib
Folium
Interactive maps
Dashboard
Gradio
Backend
FastAPI
Pydantic
Data Source Integration
Open-Meteo API
Development
Google Colab
Git
GitHub
📂 Project Structure
FLOODWISE-AI/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── FLOODWISE_AI_Main.ipynb
│
├── src/
│
├── models/
│   └── floodwise_model.pkl
│
├── backend/
│   └── backend_api.py
│
├── frontend/
│
├── gis/
│
├── docs/
│
├── README.md
├── requirements.txt
└── .gitignore
🚀 Prototype Workflow
User Input
   ↓
Rainfall + Drainage + Elevation
+ Previous Water + Blockage
   ↓
Random Forest Model
   ↓
Flood Probability
   ↓
Risk Classification
   ↓
Estimated Water Depth
   ↓
Dashboard Visualization
🎯 Current Prototype

The current version demonstrates:

AI-based flood risk prediction
0–3 hour nowcasting
Water-depth estimation prototype
Drainage blockage simulation
Safer-location identification
Interactive GIS visualization
Weather-data integration
Gradio-based dashboard
FastAPI backend prototype
🔬 Future Development

The long-term goal is to transform FLOODWISE AI into a real-world urban flood intelligence platform.

Planned improvements include:

Real-time rainfall data
Real historical flood datasets
High-resolution GIS layers
Digital Elevation Models
Drainage-network modelling
Hydrological and hydraulic modelling
Real road-network based safe-route navigation
Flood heatmaps
Real-time alerts
Bengali + English interface
Mobile-responsive web application
Explainable AI dashboard
Authority/admin dashboard
Live IoT water-level sensor integration
⚠️ Important Disclaimer

FLOODWISE AI is currently a prototype research and portfolio project.

The current machine-learning model uses synthetic/prototype data and has not been validated for operational flood forecasting.

Predicted water depth and flood probability should therefore not be used as an emergency decision-making system.

Real-world deployment would require validated datasets, calibrated hydrological/hydraulic models, reliable sensor/weather feeds, extensive testing, and domain-expert validation.

🌍 Project Origin

FLOODWISE AI was initially developed around the Smart India Hackathon problem statement SIH26085 – Urban Flood Nowcasting System (Drainage and Rainfall Coupling).

The project is currently being developed further as an independent technical portfolio project.

👩‍💻 Developer

Suparna Dey

B.Tech CSE — Cyber Security

Interested in:

Artificial Intelligence & Machine Learning
Data Science
Cyber Security
Intelligent Systems
AI Engineering
⭐ Vision

Build an intelligent urban flood early-warning system that turns environmental data into understandable, actionable risk information.

Project Status

🟡 Prototype / Active Development

More features and real-world data integrations are planned.
