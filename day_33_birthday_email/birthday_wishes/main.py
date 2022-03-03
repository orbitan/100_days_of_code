import random
import smtplib
from csv import DictReader
from datetime import date

TODAY = date.today()
DAY = TODAY.day
MONTH = TODAY.month
BIRTHDAY_CHILD = []
TEXT_FILES = ["wish_1.txt", "wish_2.txt"]

#  Open CSV File and get the Birthday Child
with open("dates.csv") as birthday_dates:
    csv_dict_reader = DictReader(birthday_dates)
    for row in csv_dict_reader:
        month, day = row['month'], row['day']
        if int(month) == MONTH and int(day) == DAY:
            BIRTHDAY_CHILD.append(row['name'])

#  Replace text
file = random.choice(TEXT_FILES)
with open(file) as text_file:
    file_text = text_file.read()
    file_text = file_text.replace('[name]', BIRTHDAY_CHILD[0])


def email_to_the_birthday_child(message):
    my_email = "sarah97hehn@outlook.de"
    my_password = "coctail1212"
    to_addrs = "sarah-hehn@outlook.de"
    with smtplib.SMTP("smtp.outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(my_email, to_addrs, f'Subject: Quote\n\n{message}')
        connection.close()


email_to_the_birthday_child(file_text)
