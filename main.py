import requests
from requests.models import Response

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USERNAME = "myomyintaung"
TOKEN = "adfadsfesdfasdfasdfa"

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

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Habit",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
}

response = requests.post(
    url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
