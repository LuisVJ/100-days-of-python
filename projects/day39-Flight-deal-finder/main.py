from flight_data import FlightData
from os import getenv
from dotenv import load_dotenv
from data_manager import DataManager
import datetime


load_dotenv(".env")

TEKILA_API = getenv("TEQUILA_API")
SHEETY_TOKEN = getenv("SHEETY_TOKEN")

DATA_MANAGER = DataManager(SHEETY_TOKEN)
FLIGHT_DATA = FlightData(TEKILA_API)

# Update IATA codes if needed
data = DATA_MANAGER.get_data()
for entry in data:
    if entry["iataCode"] == "":
        code = FLIGHT_DATA.get_city_code(entry["city"])
        DATA_MANAGER.update_code(entry, code)


# search for flights
today = datetime.datetime.today()
date_to = today + datetime.timedelta(days= 6 * 30)
dates = {
    "date_from": today.strftime("%d/%m/%Y"),
    "date_to": date_to.strftime("%d/%m/%Y")
}

for entry in data:
    flight = FLIGHT_DATA.search_cheap_flight(entry, dates)

    if flight and flight["price"] < entry["lowestPrice"]:
        # Send message
        print(
            f'Low price alert! Only  €{flight["price"]} to fly from {flight["city_from"]}-{flight["airport_from"]} to {flight["city_to"]}-{flight["airport_to"]}, from {flight["out_date"]} to {flight["return_date"]}.'
        )

# Implement notifications with telegram bot