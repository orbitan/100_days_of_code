import requests
from datetime import datetime
import smtplib

MY_LAT = -24.0
MY_LNG = -32.0

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


#  If sun set and ISS position is close, send an email
def email_notification():
    message = "ISS may soon be visible your position."
    my_email = "sarah97hehn@outlook.de"
    my_password = "coctail1212"
    to_addrs = "sarah-hehn@outlook.de"
    with smtplib.SMTP("smtp.outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(my_email, to_addrs, f'Subject: ISS\n\n{message}')
        connection.close()


#  Get the current position of iss
ISS_API_response = requests.get("http://api.open-notify.org/iss-now.json")
data = ISS_API_response.json()
iss_lat = data["iss_position"]["latitude"]
iss_lng = data["iss_position"]["longitude"]

iss_lat = float(iss_lat)
iss_lng = float(iss_lng)
print(iss_lat)

#  Get sunset
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(":")[0]
sunset = data["results"]["sunset"].split('T')[1].split(":")[0]

now = datetime.now()
current_hour = now.hour

#  Compare it to local position
visible = False
if current_hour < int(sunrise) or current_hour > int(sunset):
    if iss_lat - 5.0 < MY_LAT < iss_lat + 5.0:
        visible = True
        if iss_lng - 5.0 < MY_LNG < iss_lng + 5.0:
            visible = True
        else:
            visible = False
    if visible:
        print("ISS may be visible from your current location")
        email_notification()
