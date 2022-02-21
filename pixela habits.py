import requests
import time


pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "drorlotantan"
TOKEN = "dragondror"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "handstands",
    "unit": "minuets",
    "type": "int",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
today = time.strftime("%Y%m%d")
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

post_config = {
    "date": today,
    "quantity": "5",
}

# response = requests.post(url=pixel_endpoint, json=post_config, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
update_config = {
    "quantity": "10",
}
# response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
# print(response.text)