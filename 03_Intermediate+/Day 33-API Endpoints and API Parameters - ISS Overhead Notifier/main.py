from datetime import datetime
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()


longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)

MY_LAT = -26.204103
MY_LONG = 28.047304

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']


sunrise_hour = int(sunrise.split('T')[1].split(':')[0])
sunset_hour = int(sunset.split('T')[1].split(':')[0])

time_now = datetime.now()

# if the ISS is close to my current position
# and it is currently dark
# Then email me to tell me to look up
# BONUS: run the code every 60 seconds

