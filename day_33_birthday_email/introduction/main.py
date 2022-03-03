import random
import smtplib
import datetime as dt
import os


#  Outlook: outlook.office365.com
def email_to_myself(message):
    my_email = "sarah97hehn@outlook.de"
    my_password = "coctail1212"
    to_addrs = "sarah-hehn@outlook.de"
    with smtplib.SMTP("smtp.outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(my_email, to_addrs, f'Subject: Quote\n\n{message}')
        connection.close()


def datetime_module():
    now = dt.datetime.now()
    day = now.weekday()
    if day == 3:
        quotes()


def quotes():
    with open("quotes.txt") as quote:
        lines = quote.read().splitlines()
        my_line = random.choice(lines)
        # email_to_myself(my_line)





datetime_module()
