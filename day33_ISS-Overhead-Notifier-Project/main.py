import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 6.524379
MY_LONG = 3.379206
MY_EMAIL = "desoyee@gmail.com"
PASSWORD = "wtvyqllmhffvuggh"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

current_hour = datetime.now().hour

while True:
    time.sleep(60)
    if MY_LAT-5 <= iss_latitude and MY_LONG-5 <= iss_longitude and current_hour >= sunset or current_hour <= sunrise:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="desoyedami@gmail.com",
                                msg="Subject: ISS\n\nThe ISS is above you in the sky."
                                )
