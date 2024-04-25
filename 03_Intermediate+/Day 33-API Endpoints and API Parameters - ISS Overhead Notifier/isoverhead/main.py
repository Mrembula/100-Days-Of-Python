import requests
import smtplib
import time
import os
from datetime import datetime
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

MY_LAT = -26.204103   # Your latitude
MY_LONG = 28.047304  # Your longitude


# If the ISS is close to my current position
def is_within_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if 23 < iss_longitude < 33 and -30 < iss_latitude < -20:
        return True
    return False


# and it is currently dark
def check_sunset():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    return False


time_now = datetime.now()


# Then send me email to tell me to look up.
my_email = os.getenv('EMAIL')
to_sender = os.getenv("MY_EMAIL")
while True:
    if is_within_range() and check_sunset():
        with smtplib.SMTP("smtp.gmail.com") as server:
            password = os.getenv('GMAIL_PASS')

            server.login(user=my_email, password=password)
            server.sendmail(from_addr=my_email, to_addrs=to_sender,
                        msg="Subject: Look up\n\n The ISS is near your location look up\n"
                            "Look up!!")
    # BONUS: run the code every 60 seconds.

    elif not check_sunset():
        print("Looks like it's still light. The sun hasn't set yet")
    elif not is_within_range():
        print(f"The ISS is not near your location ISS current location")
    time.sleep(60)




