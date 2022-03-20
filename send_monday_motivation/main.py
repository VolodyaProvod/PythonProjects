import smtplib
import datetime as dt
import random

# that's real mail, you can run project and use it, just change sendmail to yours
MY_EMAIL = "testmailbypython@gmail.com"
MY_PASSWORD = "3AP-ESw-ixx-pQw"

today_is = dt.datetime.now().weekday()
if today_is == 0:
    with open("quotes.txt", "r") as file:
        text = random.choice(file.readlines())
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="achapovsky@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{text}")
