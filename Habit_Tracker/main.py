import requests
from datetime import date


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "juujrtfpl5mgtjb8vmfle;5"
USERNAME = "provod"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

GRAPH_ID = "mygraph"

grap_params = {
    "id": GRAPH_ID,
    "name": "Study time",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",
}

my_header = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=grap_params, headers=my_header)
# print(response.text)

PIXEL_INSERT_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today_in_format = str(date.today()).replace("-", "")

post_pixel_params = {
    "date": today_in_format,
    "quantity": "65",
}

# response = requests.post(url=PIXEL_INSERT_ENDPOINT, json=post_pixel_params, headers=my_header)
# print(response.text)

PIXEL_UPDATE_ENDPOINT = f"{PIXEL_INSERT_ENDPOINT}/{today_in_format}"
post_pixel_params_2 = {
    "date": today_in_format,
    "quantity": "75",
}

# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=post_pixel_params_2, headers=my_header)
# print(response.text)
#
# response = requests.delete(url=PIXEL_UPDATE_ENDPOINT, headers=my_header)
# print(response.text)