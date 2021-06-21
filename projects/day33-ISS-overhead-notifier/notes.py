import requests
import datetime as dt
# This library will allow us to make requests to APIs

response = requests.get(url="http://api.open-notify.org/iss-now.json")

if response.status_code != 200:
    # Bad response from API
    # information on status codes
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    # https://httpstatuses.com/
    pass

response.raise_for_status() # raise an error for specific request status code

# to access the data from a succesful request
data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (latitude, longitude)
print(iss_position)

# Another example. sunset times

response = requests.get(f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0")
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"]
print(sunrise)

time_now = dt.datetime.now()
print(time_now)