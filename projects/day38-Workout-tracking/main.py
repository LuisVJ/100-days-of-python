import requests
from dotenv import load_dotenv
from os import getenv
import datetime
import json


load_dotenv(".env")

with open("user-config.json") as f:
    config = json.load(f)

APP_ID = getenv("NUTRI_ID")
API_KEY = getenv("NUTRI_API")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = config["sheet_url"]
SHEETY_TOKEN = getenv("SHEETY_TOKEN")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": "cycled 15 kilometers and ran 5 km",
    "gender": config["gender"],
    "weight_kg": config["weight"],
    "height_cm": config["height"],
    "age": config["age"]
}

response = requests.post(
    url=EXERCISE_ENDPOINT,
    headers=headers,
    json=parameters
)

data = response.json()["exercises"]

# Get and format current time
current_time = datetime.datetime.now()
date = current_time.strftime("%d/%m/%Y")
time = current_time.strftime("%H:%M:%S")

################ Post data into the sheet with sheety API ###################

sheet_headers = {
    "Authorization",
    "Bearer " + SHEETY_TOKEN
}
for exercise in data:
    row = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }        
    }
    print(row)

    sheet_response = requests.post(
        url=SHEET_URL,
        json=row
    )

    print(sheet_response.status_code)