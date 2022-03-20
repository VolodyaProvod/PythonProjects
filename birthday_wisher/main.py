import smtplib
import datetime as dt
import random
import pandas


MY_EMAIL = "testmailbypython@gmail.com"
MY_PASSWORD = "3AP-ESw-ixx-pQw"
today = dt.datetime.now().today()
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
birthdays = {row.email: {
    "Name": row["name"],
    "Year": row.year,
    "Month": row.month,
    "Day": row.day}
             for (index, row) in pandas.read_csv("birthdays.csv").iterrows()}

for record in birthdays:
    if birthdays[record]["Month"] == today.month and birthdays[record]["Day"] == today.day:
        with open(f"letter_templates/{random.choice(letters)}", "r") as file:
            text = file.read().replace("[NAME]", birthdays[record]["Name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="achapovsky@gmail.com",
                msg=f"Subject:Happy Birthday!\n\n{text}")
