import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = 'mrembula1642'
TOKEN = 'vfcsw3456ythji89ikjhgft'
GRAPH_ID = 'graph01'
DATE = 'today.strftime("%Y%m%d")'

user_params = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPH_ID,
    'name': 'Coding Hours',
    'unit': 'hr',
    'type': 'float',
    'color': 'momiji'
}

header = {
    'X-USER-TOKEN' : TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_data = {
    'date': DATE,
    'quantity': input("How many hours you coded today? "),
    'optionalData':input("What language you used today? ")
}

# response = requests.post(url=pixel, json=pixel_data, headers=header)
# print(response.text) # did run, you have to join pixela as a supporter

# Put simply rewrite or overwrites data
pixel_put_del = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"    # for the given date

# Change data
pixel_put_data = {
    'quantity': '10.5'
    # Still using python though
}
requests.put(url=pixel_put_del, headers=header, json=pixel_put_data)

# delete data
requests.delete(url=pixel_put_del, headers=header)