import joblib
import pandas as pd

def _load_model():
    """Load a machine learning model from a specified path."""
    return joblib.load("models/random_forest_model.joblib")

def preprocess(data):
    """Preprocess the input DataFrame for prediction."""
    # Example preprocessing steps (these should match the training preprocessing)
    df = pd.DataFrame([data])
    df["Stage_fear"] = df["Stage_fear"].map({"Yes": 1, "No": 0})
    df["Drained_after_socializing"] = df["Drained_after_socializing"].map({"Yes": 1, "No": 0})
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
