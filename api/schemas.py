from pydantic import BaseModel, Field

class PersonalityInput(BaseModel):
    time_spent_alone: float = Field(..., alias="Time spent alone", description="Average hours spent alone per day")
    stage_fear: str = Field(..., alias="Stage fear", description="Fear of public speaking (Yes/No)")
    social_event_attendance: float = Field(..., alias="Social event attendance", description="Average number of social events attended per month")
    going_outside: float = Field(..., alias="Going outside", description="Average hours spent outside home per day")
    drained_after_socializing: str = Field(..., alias="Drained after socializing", description="Feeling drained after socializing (Yes/No)")
    friends_circle_size: float = Field(..., alias="Friends circle size", description="Number of close friends")
    post_frequency: float = Field(..., alias="Post frequency", description="Average number of social media posts per week")

    model_config = {"populate_by_name": True}

class PersonalityOutput(BaseModel):
    personality: str
    confidence: float