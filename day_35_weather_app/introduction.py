import requests

my_api = "0eff964ffcc2a12c5c73ca7d9c59f11a"
open_weather_map_url = "http://api.openweathermap.org/data/2.5/weather?q={city name},{country short}&APPID={API key}"
one_call = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API key}"


def open_weather():
    new_string = open_weather_map_url.replace("{API key}", my_api)
    new_string = new_string.replace("{city name}", "saarbruecken")
    new_string = new_string.replace("{country short}", "de")


def get_one_call_page(latitude, longitude):
    one_string = one_call.replace("{lat}", "49.234779")
    one_string = one_string.replace("{lon}", "6.994400")
    one_string = one_string.replace("{API key}", my_api)
    return one_string

result = requests.get(get_one_call_page(1, 2))
response = result.json()
#  print(response["current"]["weather"][0]["description"])