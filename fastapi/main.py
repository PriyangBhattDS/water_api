import joblib
import pandas as pd
from fastapi import FastAPI
from water_datamodel import Water

app = FastAPI(
    title= "Water Potability Prediction",
    description="Predicting water Potability")

model = joblib.load('randomforest_model.pkl')

@app.get("/")
def index():
    return "Welcome to Water Potability Prediction FastAPI"


@app.post("/predict")
def model_predict(water:Water):
    sample = pd.DataFrame({
        'Hardness': water.Hardness,
        'Solids': water.Solids,
        'Chloramines': water.Chloramines,
        'Conductivity': water.Conductivity,
        'Organic_carbon': water.Organic_carbon,
        'Turbidity': water.Turbidity,
        'ph': water.ph,
        'Sulfate': water.Sulfate,
        'Trihalomethanes': water.Trihalomethanes
    }, index=[0])
    # Load the RandomForest model once when the application starts

    predicted_value = model.predict(sample)
    # Print result
    if predicted_value == 1:
        return "Water is Consumable"
    else:
        return "Water is not consumable"

