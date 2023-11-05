import requests
from datetime import datetime

APP_ID = "b547e9e2"
APP_KEY = "6267048aaafd4c4248a81b8689aa4e16"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query_input = {
    "query": input("What exercise did you do today? "),
    "gender": "male",
    "weight_kg": 52,
    "height_cm": 167.64,
    "age": 23
}
response = requests.post(url=exercise_endpoint, json=query_input, headers=HEADERS)
data = response.json()['exercises']

date = datetime.now()
today_date = date.strftime("%d/%m/%Y")
today_time = date.strftime("%X")
new_exercise = {
  "workout": {
      "date": f"{today_date}",
      "time": f"{today_time}",
      "exercise": f"{data[0]['name'].title()}",
      "duration": data[0]['duration_min'],
      "calories": f"{data[0]['nf_calories']}",
    }
}
headers = {"Authorization": "Bearer lihjsewe9084u349p832iujejkhe"}
sheet_endpoint = "https://api.sheety.co/56f881178826c082779c1fd07d28539c/myWorkouts/workouts"
sheet_response = requests.post(url=sheet_endpoint, json=new_exercise, headers=headers)
