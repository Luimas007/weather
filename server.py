# server.py
from fastapi import FastAPI
from weather_scraper import get_current_weather
from weather_predictor import predict_next_day_weather

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Predictive Weather API"}

@app.get("/current/{city}")
def get_weather(city: str):
    weather = get_current_weather(city)
    return weather

@app.get("/predict/{city}")
def predict_weather(city: str):
    weather = get_current_weather(city)
    if "error" in weather:
        return weather

    prediction = predict_next_day_weather(weather)
    return {
        "city": city,
        "current_weather": weather,
        "prediction": prediction
    }
