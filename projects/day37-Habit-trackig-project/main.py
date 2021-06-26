import requests
from dotenv import load_dotenv
from os import getenv
import datetime

from requests.models import Response

load_dotenv(".env")

PIXELA_TOKEN = getenv("PIXELA_TOKEN")
USERNAME = "luisv"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": "luisv",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# **** User creation *****
# response = requests.post(url=pixela_endpoint, json=user_params )
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "sora",
}

# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
# print(response.text)

reading_graph_endpoint = f"{graph_endpoint}/graph1"

today = datetime.date.today().strftime('%Y%m%d')
yesterday = datetime.date.today() - datetime.timedelta(days=1)
yesterday = yesterday.strftime('%Y%m%d')

print(yesterday)

graph1_config = {
    "date": yesterday,
    "quantity": "15",
    "optionalData": "{\"Book\":\"The pragmatic programmer\"}"
}

# response = requests.post(
#     url=reading_graph_endpoint, headers=headers, json=graph1_config
# )
# print(response.text)
update_endpoint = f"{reading_graph_endpoint}/{yesterday}"

update_config = {
    "quantity": "31",
    "optionalData": "{\"Book\":\"The pragmatic programmer\"}"
}

response = requests.put(url=update_endpoint, headers=headers, json=update_config)

print(response.text)