import datetime as dt
import smtplib
import pandas
import random

PLACEHOLDER = "[NAME]"
MY_EMAIL = "desoyee@gmail.com"
PASSWORD = "wtvyqllmhffvuggh"

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
current_date = dt.datetime.now()
year = current_date.year
month = current_date.month
day = current_date.day

df = pandas.read_csv("birthdays.csv")
data = df.to_dict(orient='records')

i = 0
while i < len(data):
    if data[i]["year"] == year:
        recipient_name = data[i]["name"]
        recipient_mail = data[i]["email"]

        # 3. If step 2 is true, pick a random letter from letter templates
        # and replace the [NAME] with the person's actual name from birthdays.csv
        n = random.randint(1, 3)
        with open(f"letter_templates/letter_{n}.txt") as letter:
            read_letter = letter.read()
            new_letter = read_letter.replace(PLACEHOLDER, recipient_name)

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=recipient_mail,
                                msg=f"Subject: Happy Birthday\n\n{new_letter}")
    i += 1
