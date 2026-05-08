from src.pipeline import predict

def test_extrovert():
    data = {
        "time_spent_alone": 1.0,
        "stage_fear": "No",
        "social_event_attendance": 8.0,
        "going_outside": 6.0,
        "drained_after_socializing": "No",
        "friends_circle_size": 12.0,
        "post_frequency": 7.0
    }
    result = predict(data)
    assert result["personality"] == "Extrovert"
    print(result)

def test_introvert():
    data = {
        "time_spent_alone": 9.0,
        "stage_fear": "Yes",
        "social_event_attendance": 1.0,
        "going_outside": 0.0,
        "drained_after_socializing": "Yes",
        "friends_circle_size": 1.0,
        "post_frequency": 1.0
    }
    result = predict(data)
    assert result["personality"] == "Introvert"
    print(result)