import os
import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

email = os.getenv('EMAIL')
my_email = os.getenv('MY_EMAIL')
PURCHASE = 130

amazon = ("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_3?adgrpid"
          "=158527346836&dib=eyJ2IjoiMSJ9.2bTkAlQ1-EFEsdfcFbCM7djkeoOsZU7fq_d646rg5f75oxM8-X-AzkhXdMx8V62zNDFCX0Dcv6"
          "-PxlK3eDlt1ib-N7y3Qm_nDV8L4rIs6CuNZb1J4MYM124m2eFJwCEpI30oCAe_Zi_rEo2Prm63hRkGZycKkQe5mWhLpljNKs4eFnoBB7iPmpYG3AMqXLjIJkMZKC59RkP0kYJjez9gxqenegeYOOAkt0u4mQzJoDk._R_8QcTuwy07cCr4T2mjEv9nBhUmEHPAZTAFy7RSxT0&dib_tag=se&gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFo_KgGlFSDyyE8E8aP8fG7u_bashWvWPcFPVSFKx1882_3c-svy-UPBoCUq4QAvD_BwE&hvadid=689757507033&hvdev=c&hvlocphy=1029034&hvnetw=g&hvqmt=b&hvrand=15277520036071206745&hvtargid=kwd-361652192637&hydadcr=17669_13650182&keywords=instant%2Bpot%2Bduo%2B7&qid=1713083604&sr=8-3&th=1")

response = requests.get(amazon)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
price = float(soup.select_one(".a-section .a-spacing-none span .a-offscreen").getText().strip('$'))

if price <= PURCHASE:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        password = os.getenv('GMAIL_PASS')

        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=my_email,
        msg="Subject:Amazon Price Alert!\nInstant Pot Duo 7-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, "
            "Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, "
            f"6 Quart now {price}\n{amazon}")



