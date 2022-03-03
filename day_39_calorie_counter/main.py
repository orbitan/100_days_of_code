import requests

APP_ID = "08142b28"
API_KEY = "0574f7bf8cf30ed2ab9e9e992e0eea84"
LINK = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}
qu = {
 "query":"ran 3 miles",
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}


response = requests.post(url=f"{LINK}", data=qu,  headers=headers)
print(response.json())