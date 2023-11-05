import requests

parameters = {
    "lat": 6.5244,
    "lon": 3.3792,
    "appid": "50b0779474aa4883c2a9afe2825fb3c6"
}
response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
data = response.json()
print(data)
