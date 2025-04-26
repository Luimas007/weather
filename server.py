from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from weather_scraper import get_current_weather
from weather_predictor import predict_next_day_weather

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to allow frontend calls from different domains (like GitHub Pages)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins (you can restrict this if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods like GET, POST, etc.
    allow_headers=["*"],  # Allow all headers
)

# Define root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Predictive Weather API"}

# Define route for current weather
@app.get("/current/{city}")
def get_weather(city: str):
    weather = get_current_weather(city)
    return weather

# Define route for weather prediction
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
