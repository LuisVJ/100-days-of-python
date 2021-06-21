import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 42.388251 # Your latitude
MY_LONG = -5.788597 # Your longitude

MY_EMAIL = "my_email@gmail.com"
MY_PASSWORD = "randpass2345"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_close(latitude, longitude):
    return abs(MY_LAT - latitude) <= 5 and abs(MY_LONG - longitude) <= 5
        


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()


sunrise_dt = datetime.strptime(
    data["results"]["sunrise"], '%Y-%m-%dT%H:%M:%S%z'
    ).replace(tzinfo=None)
sunset_dt = datetime.strptime(
    data["results"]["sunset"], '%Y-%m-%dT%H:%M:%S%z'
    ).replace(tzinfo=None)

# sunset_time = sunset_dt.strftime("%H:%M:%S")
# sunrise_time = sunrise_dt.strftime("%H:%M:%S")

def is_dark():
    time_now = datetime.utcnow().replace(tzinfo=None)
    return time_now < sunrise_dt or time_now > sunset_dt

#If the ISS is close to my current position
# and it is currently dark
while True:
    time.sleep(60)
    if is_iss_close(iss_latitude, iss_longitude) and is_dark():
        # Then send me an email to tell me to look up.
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look UP\n\nThe ISS is above you."
        )

