import joblib
import pandas as pd

def _load_model():
    """Load a machine learning model from a specified path."""
    return joblib.load("models/random_forest_model.joblib")

def preprocess(data):
    """Preprocess the input DataFrame for prediction."""
    df = pd.DataFrame([data])
    df["stage_fear"] = df["stage_fear"].str.capitalize().map({"Yes": 1, "No": 0})
    df["drained_after_socializing"] = df["drained_after_socializing"].str.capitalize().map({"Yes": 1, "No": 0})
    df = df.rename(columns={
        "time_spent_alone": "Time_spent_Alone",
        "stage_fear": "Stage_fear",
        "social_event_attendance": "Social_event_attendance",
        "going_outside": "Going_outside",
        "drained_after_socializing": "Drained_after_socializing",
        "friends_circle_size": "Friends_circle_size",
        "post_frequency": "Post_frequency"
    })
    return df

def predict(data):
    """Predict the personality type based on the input data."""
    model = _load_model()
    preprocessed_data = preprocess(data)
    prediction = model.predict(preprocessed_data)
    probability = model.predict_proba(preprocessed_data)

    label = "Extrovert" if prediction[0] == 1 else "Introvert"
    confidence = round(float(probability[0][prediction[0]]), 4)

    return {"personality": label, "confidence": confidence}
