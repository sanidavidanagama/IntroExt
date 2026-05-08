from src.pipeline import predict

def test_introvert(): 
    data = {
        "Time_spent_Alone": 1.0,
        "Stage_fear": "No",
        "Social_event_attendance": 8.0,
        "Going_outside": 6.0,
        "Drained_after_socializing": "No",
        "Friends_circle_size": 12.0,
        "Post_frequency": 7.0
    }
    result = predict(data)
    assert result["personality"] == "Extrovert"
    print(result)

def test_extrovert():
    data = {
        "Time_spent_Alone": 9.0,
        "Stage_fear": "Yes",
        "Social_event_attendance": 1.0,
        "Going_outside": 0.0,
        "Drained_after_socializing": "Yes",
        "Friends_circle_size": 1.0,
        "Post_frequency": 1.0
    }   
    result = predict(data)
    assert result["personality"] == "Introvert"
    print(result)