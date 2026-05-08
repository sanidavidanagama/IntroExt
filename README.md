# IntroExt

Predict whether a person is an introvert or an extrovert from a small set of behavioral and social features. The project includes exploratory data analysis, preprocessing, model comparison, and a FastAPI backend for inference.

## Contents

- [Overview](#overview)
- [Live API](#live-api)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Run The API](#run-the-api)
- [Endpoints](#endpoints)
- [Field Descriptions](#field-descriptions)
- [Tech Stack](#tech-stack)
- [Project Artifacts](#project-artifacts)

## Overview

The model development work was completed in the `feat/eda-and-model` branch:

- [EDA and preprocessing](https://github.com/sanidavidanagama/IntroExt/blob/feat/eda-and-model/notebooks/eda-and-preprocessing.ipynb)
- [Random Forest](https://github.com/sanidavidanagama/IntroExt/blob/feat/eda-and-model/notebooks/random_forest.ipynb)
- [XGBoost](https://github.com/sanidavidanagama/IntroExt/blob/feat/eda-and-model/notebooks/xgboost.ipynb)

Two machine learning models were trained: a Random Forest classifier and an XGBoost classifier. Random Forest was selected for deployment because it achieved the best balance of performance and stability:

- Higher test accuracy (91.6%) and AUC (0.961)
- Balanced feature importance across all 7 features
- Minimal overfitting with only a 1.5% train/test gap

The backend is built with FastAPI and serves predictions from the deployed Random Forest model.

Random Forest was chosen as the final model because it generalized better than the alternative while remaining easy to interpret. Its test metrics were stronger, the feature contributions were distributed across the full input set, and the train/test performance gap stayed small enough to suggest limited overfitting.

## Live API

Base URL: `https://introext-production.up.railway.app`

- Swagger UI: `https://introext-production.up.railway.app/docs`
- ReDoc: `https://introext-production.up.railway.app/redoc`


## Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)

## Setup


Clone the repository
```bash
git clone https://github.com/sanidavidanagama/IntroExt.git
cd IntroExt
```

Create a virtual environment
```bash
uv venv
```

Activate virtual env
```bash
# Windows PowerShell:
.venv\Scripts\Activate.ps1
```

Install dependencies
```bash
uv sync
```

## Run The API Locally

```bash
uv run uvicorn api.main:app --reload
```

The API will be available at `http://localhost:8000`.

## Endpoints

### `GET /`

Health check.

Response:

```json
{
	"message": "IntroExt API is running"
}
```

### `POST /predict`

Predict personality type.

Request body:

```json
{
	"Time spent alone": 8.0,
	"Stage fear": "Yes",
	"Social event attendance": 1.0,
	"Going outside": 1.0,
	"Drained after socializing": "Yes",
	"Friends circle size": 2.0,
	"Post frequency": 1.0
}
```

Response:

```json
{
	"personality": "Introvert",
	"confidence": 0.8665
}
```

## Field Descriptions

| Field | Type | Constraints | Description |
|---|---|---|---|
| Time spent alone | float | 0 - 24 | Hours spent alone per day |
| Stage fear | string | Yes / No | Whether the person has stage fear |
| Social event attendance | float | >= 0 | Social events attended per month |
| Going outside | float | >= 0 | Times going outside per week |
| Drained after socializing | string | Yes / No | Feels drained after socializing |
| Friends circle size | float | >= 0 | Number of close friends |
| Post frequency | float | >= 0 | Social media posts per week |

## Tech Stack

- Model: Scikit-learn Random Forest
- API: FastAPI
- Deployment: Railway
- Dependency management: uv

## Project Artifacts

- [API entrypoint](api/main.py)
- [Request and response schemas](api/schemas.py)
- [Prediction pipeline](src/pipeline.py)
- [Tests](tests/test_pipeline.py)
- [Trained models](models/)
- [Data](data/)