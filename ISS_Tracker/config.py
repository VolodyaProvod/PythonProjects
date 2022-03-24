import smtplib

# that's real mail, you can run project and use it, just change sendmail to yours
MY_EMAIL = "testmailbypython@gmail.com"
MY_PASSWORD = "3AP-ESw-ixx-pQw"


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="achapovsky@gmail.com",
            msg=f"Subject:ISS is coming☝\n\nLook at the sky!")
