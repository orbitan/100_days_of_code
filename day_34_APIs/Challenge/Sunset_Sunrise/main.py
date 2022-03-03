import requests
from datetime import datetime


MY_LAT = 49.234779
MY_LNG = 6.994400

#  6:44am
#  4:48pm

parameters = {
    "lat": 52.520008,
    "lng": 13.404954,
    "formatted":  0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(":")[0]
sunset = data["results"]["sunset"].split('T')[1].split(":")[0]

print(sunrise, sunset)

time_now = datetime.now
