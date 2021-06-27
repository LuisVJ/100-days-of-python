import requests

class FlightData:
    def __init__(self, api_key):
        self.locations_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.api_key = api_key
        self.from_code = "MAD"
        self.header = {
            "apikey": self.api_key
        }



    def get_city_code(self, city):
        parameters = {
            "term": city,
            "location_types": "city"
        }

        response = requests.get(
            url=self.locations_endpoint,
            headers=self.header,
            params=parameters
        )
        print(response.status_code)
        data = response.json()
        city_code = data["locations"][0]["code"]

        return city_code

    
    def search_cheap_flight(self, city, dates):

        parameters = {
            "fly_from": self.from_code,
            "fly_to": city["iataCode"],
            "date_from": dates["date_from"],
            "date_to": dates["date_to"],
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            # "sort": "price",
            # "limit": 5
        }
        response = requests.get(
            url=self.search_endpoint,
            headers=self.header,
            params=parameters
        )
        print(response.status_code)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {city['city']}")
            return

        flight_data = {
            "price": data["price"],
            "city_from": data["cityFrom"],
            "airport_from": data["route"][0]["flyFrom"],
            "city_to": data["cityTo"],
            "airport_to": data["route"][0]["flyTo"],
            "out_date": data["route"][0]["local_departure"].split("T")[0],
            "return_date": data["route"][1]["local_departure"].split("T")[0]
        }
        return flight_data