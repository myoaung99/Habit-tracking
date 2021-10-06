import requests
from datetime import datetime
from requests.api import head
from requests.models import Response

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USERNAME = "myomyintaung"
TOKEN = "adfadsfesdfasdfasdfa"
GRAPH_ID = "graph1"

# Creating pixela account with POST method
user_paramas = {
    "token": "adfadsfesdfasdfasdfa",
    "username": "myomyintaung",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_paramas)
# print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN
}

# Creating Graph with POST Method
graph_creating_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_creating_config = {
    "id": GRAPH_ID,
    "name": "Coding Habit",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
}

# response = requests.post(
#     url=graph_creating_endpoint, json=graph_creating_config, headers=headers)
# print(response.text)

pixel_creating_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(2020, 10, 5)

# We can change to any format of Date with strftime() method

# Creating pixel With POST Method
pixel_creating_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

# response = requests.post(url=pixel_creating_endpoint,
#                          json=pixel_creating_config, headers=headers)
# print(response.text)


# Updating the exisiting pixel with PUT Method
pixel_updating_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_updating_config = {
    "quantity": "1",

}

# response = requests.put(url=pixel_updating_endpoint,
#                         json=pixel_updating_config, headers=headers)
# print(response.text)

# Deleting the exisiting pixel wiht DELETE method
piexl_deleting_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=piexl_deleting_endpoint, headers=headers)
print(response.text)
