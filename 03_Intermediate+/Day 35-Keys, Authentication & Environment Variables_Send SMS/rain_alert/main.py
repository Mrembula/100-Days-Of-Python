import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import find_dotenv, load_dotenv

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

weather_params = {
    "lat": 28.0436,
    "lon": -26.2023,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+19382010470",
        to="+27614986184"
    )
    print(message.status)
