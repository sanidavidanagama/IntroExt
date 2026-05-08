from fastapi import FastAPI
from pydantic import BaseModel
from src.pipeline import predict

app = FastAPI(
    title="IntroExt Personality Prediction API",
    description="API for predicting personality type (Introvert or Extrovert) based on user input features.",
    version="1.0.0"
)