from fastapi import FastAPI
from pydantic import BaseModel
from src.pipeline import predict
from api.schemas import PersonalityInput, PersonalityOutput

app = FastAPI(
    title="IntroExt Personality Prediction API",
    description="API for predicting personality type (Introvert or Extrovert) based on user input features.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to the IntroExt API! Use the /predict endpoint to get predictions."}

@app.post("/predict")
def predict_personality(data: PersonalityInput):
    print(data.model_dump())
    result = predict(data.model_dump())
    return result   