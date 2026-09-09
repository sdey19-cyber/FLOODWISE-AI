# 🌊 FLOODWISE AI

### See the flood before the street does.

**Urban Flood Nowcasting System — SIH26085** 

FLOODWISE AI is an AI-powered prototype designed to predict urban flood risk for the next 0–3 hours by coupling rainfall conditions with drainage capacity, elevation, previous water level, and drainage blockage.

The system aims to provide early flood-risk awareness and identify comparatively safer locations during heavy rainfall events.

---

## 🚨 Problem Statement

Urban flooding can occur rapidly when intense rainfall exceeds the capacity of drainage systems.

Traditional flood monitoring systems may not provide sufficiently localized and predictive information for citizens and authorities.

FLOODWISE AI addresses this problem by combining environmental and drainage-related parameters with machine learning to generate short-term flood-risk predictions.

---

## 💡 Key Features

- 🌧️ Rainfall-based flood prediction
- ⏱️ 0–3 hour flood nowcasting
- 🤖 Machine learning-based risk classification
- 🌊 Prototype water-depth estimation
- 🚧 Drainage blockage impact analysis
- 🛣️ Comparatively safer location identification
- 🗺️ GIS-ready architecture
- 📊 Explainable AI / feature importance
- 🌐 Weather-data integration
- 🖥️ Interactive Gradio dashboard

---

## 🧠 How It Works

```text
Rainfall Data
      ↓
Environmental & Drainage Parameters
      ↓
Machine Learning Model
      ↓
Flood Probability
      ↓
Risk Classification
      ↓
Water Depth Estimation
      ↓
0–3 Hour Nowcast
      ↓
Safer Location Identification
🤖 Machine Learning

The current prototype uses a:

Random Forest Classifier

Input Features
Rainfall (mm)
Drainage Capacity
Elevation (m)
Previous Water Level (m)
Drainage Blockage (%)
Output
Flood Probability
Flood / No Flood prediction
Risk Level
Prototype Estimated Water Depth
⏱️ 0–3 Hour Nowcasting

FLOODWISE AI generates a short-term flood-risk forecast for:

Hour 0
Hour 1
Hour 2
Hour 3

This allows the system to provide early warning before flood conditions become severe.

🚧 Drainage Blockage Simulation

The system can simulate how increasing drainage blockage may affect flood risk.

This can help demonstrate the relationship between:

Drainage blockage → reduced drainage capacity → increased flood risk

🛣️ Safer Location Identification

The prototype evaluates predefined locations and identifies locations with comparatively lower predicted flood probability and water depth.

Note: The current prototype identifies safer points, not real-time road navigation routes. Integration with a road-network routing system would be required for production deployment.

🗺️ GIS Integration

The architecture is designed to support GIS-based visualization of:

Flood-risk zones
Rainfall conditions
Drainage infrastructure
Elevation
Water levels
Safer locations
🛠️ Technology Stack
Category	Technology
Programming	Python
Machine Learning	Scikit-learn
Data Processing	Pandas, NumPy
Visualization	Matplotlib
Dashboard	Gradio
GIS	Folium / GIS tools
Weather Data	Weather API
Backend	FastAPI
Model	Random Forest
Development	Google Colab
📁 Project Structure
FLOODWISE-AI/
│
├── backend/
│   └── backend_api.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── frontend/
│
├── gis/
│
├── models/
│   └── floodwise_model.pkl
│
├── notebooks/
│   └── FLOODWISE_AI_Main.ipynb
│
├── src/
│
├── README.md
├── requirements.txt
└── .gitignore
🖥️ Dashboard

The interactive dashboard provides:

Flood Prediction

Users can enter environmental conditions and receive:

Flood probability
AI prediction
Risk level
Estimated prototype water depth
0–3 Hour Nowcast

The system generates short-term flood-risk predictions for the next three hours.

Safer Locations

The system identifies comparatively safer prototype locations based on predicted flood risk and prototype water-depth estimates.

⚠️ Current Prototype Limitation

The current version is a proof-of-concept prototype.

The machine-learning model has been trained using synthetic/prototype data. Therefore, the current predictions should not be interpreted as validated real-world flood probabilities or physically accurate water depths.

For real-world deployment, the system should be trained and validated using:

Historical rainfall data
Real-time rainfall observations
Drainage-network data
Digital Elevation Models (DEM)
Historical flood/water-level observations
Drainage blockage information
Hydrological and hydraulic modelling
Validated road-network data
🔮 Future Scope

Future versions can include:

📡 Real-time rainfall feeds
🛰️ Satellite and remote-sensing data
🗺️ High-resolution DEM
🚰 Real drainage-network modelling
💧 Hydrological/hydraulic simulation
📱 Mobile emergency alerts
🚗 Real road-level safe-route navigation
🧠 Advanced spatio-temporal deep learning
☁️ Cloud deployment
🏙️ City-wide flood digital twin
🎯 Objective

The long-term objective of FLOODWISE AI is to transform flood management from a reactive approach into a predictive and preventive system.

Predict early. Respond faster. Stay safer.

👩‍💻 Project

FLOODWISE AI
Urban Flood Nowcasting System
SIH26085

Developed as a prototype for Smart India Hackathon.
