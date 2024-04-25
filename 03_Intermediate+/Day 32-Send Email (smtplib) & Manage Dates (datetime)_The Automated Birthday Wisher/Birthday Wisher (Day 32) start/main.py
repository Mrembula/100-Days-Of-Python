import os
import smtplib
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

my_email = os.getenv('MY_EMAIL')
email = os.getenv('EMAIL')

with smtplib.SMTP('smtp.gmail.com') as connection:
    password =  os.getenv('GMAIL_PASS')

    connection.starttls()  # Keeps the email encrypted from outside users
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=email, to_addrs=my_email,
                        msg='Subject:Hello\n\nHello, Tebogo keep moving boza!!')


