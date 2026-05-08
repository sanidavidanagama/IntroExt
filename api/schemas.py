from pydantic import BaseModel, Field, field_validator

class PersonalityInput(BaseModel):
    time_spent_alone: float = Field(..., alias="Time spent alone", description="Number of hours spent alone per day (0-24)", ge=0, le=24)
    stage_fear: str = Field(..., alias="Stage fear", description="Whether the person has stage fear. Must be 'Yes' or 'No'")
    social_event_attendance: float = Field(..., alias="Social event attendance", description="Number of social events attended per month", ge=0)
    going_outside: float = Field(..., alias="Going outside", description="Number of times going outside per week")
    drained_after_socializing: str = Field(..., alias="Drained after socializing", description="Whether the person feels drained after socializing. Must be 'Yes' or 'No'")
    friends_circle_size: float = Field(..., alias="Friends circle size", description="Number of close friends", ge=0)
    post_frequency: float = Field(..., alias="Post frequency", description="Number of social media posts per week", ge=0)

    model_config = {"populate_by_name": True}

    @field_validator("stage_fear", "drained_after_socializing")
    @classmethod
    def validate_yes_no(cls, value):
        if value.lower() not in {"yes", "no"}:
            raise ValueError("Value must be 'Yes' or 'No'")
        return value.strip().capitalize()

class PersonalityOutput(BaseModel):
    personality: str = Field(description="Predicted personality type: 'Introvert' or 'Extrovert'")
    confidence: float = Field(description="Model confidence score between 0 and 1")