import os
import requests
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

api_key = os.getenv("NUTRI_API_KEY")
app_id = os.getenv("NUTRI_APP_ID")

WEIGHT = "45"
HEIGHT = "167.64"
GENDER = "Male"
AGE = "25"

url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("Tell me which exercises you did: ")

headers = {
    "x-app_id": app_id,
    "x-app_key": api_key,
}

parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url_endpoint, json=parameters, headers=headers)
print(response.status_code)
print(response.text)

# If submitted this way. I'm getting unauthorized error 401 and yet am logged in
# Some problems with the web API protocol
