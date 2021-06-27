import requests

class DataManager:
    def __init__(self, token):
        self.token = token
        self.endpoint = "https://api.sheety.co/a16b7367d44adb4deb6b8707ccd9c415/flightDeals/prices"
        self.headers = {
            "Authorization": "Bearer " + self.token
        }


    def get_data(self):
        get_response = requests.get(url=self.endpoint, headers=self.headers)
        print(get_response.status_code)

        return get_response.json()["prices"]


    def update_code(self, row, code):
        body = {
            "price": {
                "city": row["city"],
                "iataCode": code,
                "lowestPrice": row["lowestPrice"] 
            }
        }

        response = requests.put(
            url = f"{self.endpoint}/{row['id']}",
            json= body,
            headers= self.headers
        )
        if response.status_code != 200:
            print(f"failed to update code of {row['city']}")
        else:
            print(f"{row['city']} code updated to {code}")
    