from fastapi import FastAPI
from pydantic import BaseModel
from src.pipeline import predict

app = FastAPI(
    title="IntroExt Personality Prediction API",
    description="API for predicting personality type (Introvert or Extrovert) based on user input features.",
    version="1.0.0"
)

class PersonalityInput(BaseModel):
    Time_spent_alone: float
    Stage_feat: str
    Social_event_attendance: float
    Going_outside: float
    Drained_after_socializing: str
    Friends_circle_size: float
    Post_frequency: float
