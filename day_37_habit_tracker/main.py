import requests
from datetime import date

USERNAME = "brotkorb"
TOKEN = "kfldhjrenlk"
GRAPH_ID = "graph1"
TODAY = date.today().strftime("%Y%m%d")


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "kfldhjrenlk",
    "username": "brotkorb",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

#  response = requests.post(pixela_endpoint, json=user_params)
#  print(response.text)

graph_config = {
    "id": "graph1",
    "name": "Programming",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"
    }

headers = {
    "X-USER-TOKEN": TOKEN,
}

#  response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#  print(response.text)

graph_update = f"{graph_endpoint}/{GRAPH_ID}"



graph_update_config = {
    "date": "20220201",
    "quantity": "60"
}

#  response = requests.post(url=graph_update, json=graph_update_config, headers=headers)
#  print(response.text)

response = requests.post(url=f"{graph_update}/20220201", headers=headers)
i = 3



