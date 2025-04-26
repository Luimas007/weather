# weather_scraper.py
import requests

def get_current_weather(city: str):
    """
    Scrapes weather info from wttr.in for a given city.
    Returns temperature in Celsius and weather description.
    """
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        data = response.json()

        current_condition = data['current_condition'][0]
        temp_c = current_condition['temp_C']
        weather_desc = current_condition['weatherDesc'][0]['value']

        return {
            "temperature_c": int(temp_c),
            "description": weather_desc
        }
    except Exception as e:
        return {"error": str(e)}
