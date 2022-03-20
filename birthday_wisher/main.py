import smtplib
import datetime as dt
import random
import pandas


MY_EMAIL = "testmailbypython@gmail.com"
MY_PASSWORD = "3AP-ESw-ixx-pQw"
today = dt.datetime.now().today()
today_tuple = (today.month, today.day)
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
birthdays = {(row.month, row.day): row for (index, row) in pandas.read_csv("birthdays.csv").iterrows()}
if today_tuple in birthdays:
    birthday_person = birthdays[today_tuple]
    with open(f"letter_templates/{random.choice(letters)}", "r") as file:
        text = file.read().replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{text}")
