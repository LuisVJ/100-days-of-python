import requests
import os

API_KEY = os.environ.get("OWM_API_KEY")
ENDPOINT = "http://api.openweathermap.org/data/2.5/onecall"

coordinates = (42.387993, -5.788850)

parameters = {
    "lat": 42.387993,
    "lon": -5.788850,
    "exclude": "current,minutely,daily,alerts",
    "units": "metric",
    "lang": "sp",
    "appid": API_KEY
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

def check_weather(data):
    next_12h = data["hourly"][:12]
    for hour in next_12h:
        code = hour["weather"][0]["id"]            
        if int(code) < 700:
            return f"Bring an umbrella"

    # No rain found
    return "No rain today"

print(response.status_code)
print(check_weather(weather_data))