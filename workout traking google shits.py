import requests
from datetime import datetime

GENDER = "male"


APP_ID = "7061c79f"
API_KEY = "644c22f485e09932e9cab5c0c5f6b6fa"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# query = input("what workout you did today? ")
exercise_config = {
    "query": "ran 5 kilometers",
    "gender": GENDER,
}

response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_config)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_endpoint = "https://api.sheety.co/5c96ac968489a85ea64c068bcf60e814/workoutTracking/workouts"
add_workout = requests.post(url=sheety_endpoint, json=sheet_inputs)
print(add_workout.text)