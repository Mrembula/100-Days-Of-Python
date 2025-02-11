import os
import random
import smtplib
import datetime as dt

from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
EMAIL = os.getenv("EMAIL")

current = dt.datetime.now()

if current.weekday() == 1:
    with open('quotes.txt', 'r') as file:
        quotes_list = file.readlines()
        random_quote = random.choice(quotes_list) # choose random quotes from the list of quotes
        message, author = random_quote.split('-')

        with smtplib.SMTP('smtp.gmail.com') as connection:
            PASSWORD = os.getenv('GMAIL_PASS')

            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=EMAIL,
                                msg=f'Subject:Monday Motivational Quote\n\n{message}\n{author}')


