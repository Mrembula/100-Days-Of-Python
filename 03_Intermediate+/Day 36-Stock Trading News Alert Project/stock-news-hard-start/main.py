from datetime import datetime as dt
import os
import random
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import find_dotenv, load_dotenv

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
current_time = dt.now()
yesterday = f"{current_time.year}-{current_time.month: 03d}-{current_time.day - 1: 03d}".replace(' ', '')
day_before = f"{current_time.year}-{current_time.month: 03d}-{current_time.day - 2: 03d}".replace(' ',  '')

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

api_key = os.getenv("NEWSAPI")
stock_api_key = os.getenv("STOCKAPI")
sid = os.getenv("ACCOUNT_SID")
token = os.getenv("AUTH_TOKEN")

# STEP 1: Use https://newsapi.org/docs/endpoints/everything
news_params = {
    'q': 'tesla',
    'apiKey': api_key,
    'from': yesterday,
    'to': day_before,
}

response = requests.get(NEWS_ENDPOINT, params=news_params)
response.raise_for_status()
tesla_news = response.json()


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
"""
stock_params = {
    'function': "TIME_SERIES_DAILY",
    'symbol': STOCK,
    'apiKey': stock_api_key,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_response = response.json()
print(stock_response)
"""
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=P6XG587R2R5DRRPA"
response = requests.get(url)
response.raise_for_status()

stock_response = response.json()

# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between
# the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
yesterday_stock = stock_response["Time Series (Daily)"][yesterday]["4. close"]
day_before_stock = stock_response["Time Series (Daily)"][day_before]["4. close"]
stock_price = float(day_before_stock) - float(yesterday_stock)

# HINT 2: Work out the value of 5% of yerstday's closing stock price.
stock_percent = stock_price * float(yesterday_stock) / float(day_before_stock)

display = ''
if stock_percent >= 0:
    display = f"🟢 {stock_price:.2f}%"
else:
    display = f"🔴 {stock_price:.2f}%"


# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator
tesla_news = tesla_news['articles'][:3]


# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.
headlines =[title['title'] for title in tesla_news]
messages = [news['description'] for news in tesla_news]
choice_number = random.randint(0, len(messages) - 1)


proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ.get('PROXY_URL')}

client = Client(sid, token, http_client=proxy_client)
message = client.messages \
    .create(
    body=f"TSLA:{display}\nHeadline:{headlines[choice_number]}\nBrief:{messages[choice_number]}",
    from_="+19382010470",
    to="+27614986184"
)
print(message)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

