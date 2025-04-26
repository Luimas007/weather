# weather_predictor.py

def predict_next_day_weather(current_weather: dict):
    """
    A simple prediction logic:
    - If current temp > 25°C and sunny -> Predict "Hot and Sunny"
    - If temp < 15°C -> Predict "Cold"
    - Else -> Predict "Mild"
    """

    temp = current_weather.get('temperature_c', 20)
    description = current_weather.get('description', '').lower()

    if "rain" in description:
        forecast = "Expect Rain Tomorrow"
    elif temp > 25 and ("sun" in description or "clear" in description):
        forecast = "Hot and Sunny"
    elif temp < 15:
        forecast = "Cold and Chilly"
    else:
        forecast = "Mild and Pleasant"

    return {
        "predicted_temp": temp + 1,  # assuming slight warming
        "forecast": forecast
    }
