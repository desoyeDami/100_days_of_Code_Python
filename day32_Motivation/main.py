import datetime as dt
import random
import smtplib

with open("quotes.txt") as quotes_data:
    quotes = quotes_data.readlines()
    random_quote = random.choice(quotes)

now = dt.datetime.now()
year = now.year
week_day = now.weekday()

my_email = "desoyee@gmail.com"
password = "wtvyqllmhffvuggh"

while year < 2030:
    if week_day == 0:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="desoyedami@gmail.com",
                                msg=f"Subject: Monday Motivation\n\n{random_quote}")
