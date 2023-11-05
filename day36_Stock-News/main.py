import math
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCKAPIKEY = "OAJYVS4NNR0MPGO6"
NEWSAPIKEY = "6aea6ac3c3914ac49eb8b742549e47d0"

stock_url = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKAPIKEY
}

response = requests.get(url=stock_url, params=parameters)
data = response.json()["Time Series (Daily)"]
day = []
for key in data:
    day.append(key)
first_day = day[0]
second_day = day[1]

yesterday_closing_price = float(data[first_day]["4. close"])
day_before_yesterday_closing_price = float(data[second_day]["4. close"])
difference = yesterday_closing_price - day_before_yesterday_closing_price
percentage_difference = math.floor((difference / yesterday_closing_price) * 100)

if percentage_difference > 0:
    header = f"{STOCK} 🔺{percentage_difference}%"
else:
    header = f"{STOCK} 🔻{percentage_difference * -1}%"

params = {
        "q": STOCK.lower(),
        "from": second_day,
        "to": first_day,
        "apiKey": NEWSAPIKEY
    }

r = requests.get(url="https://newsapi.org/v2/everything", params=params)
r.raise_for_status()
r_data = r.json()

headline = []
content = []
for n in range(0, 3):
    headline.append(r_data["articles"][n]["title"])
    content.append(r_data["articles"][n]["description"])

account_sid = "AC8a6862abb703c9c56a04dc55169c4daa"
auth_token = "cd794e597f184ce37cb6ddddb2b56cfc"
client = Client(account_sid, auth_token)

for n in range(0, 3):
    message = client.messages \
                    .create(
                         body=f"\n{header}\n\nHeadline: {headline[n]}\n\nBrief: {content[n]}\n\n",
                         from_='+14159121337',
                         to='+2348164252688'
                     )
    print(message.status)
