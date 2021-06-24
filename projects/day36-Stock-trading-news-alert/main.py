from os import getenv
from dotenv import load_dotenv
import requests
import datetime

load_dotenv(".env")

NEWS_API = getenv("NEWS_API")
STOCK_API = getenv("STOCK_API")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API
}

today = datetime.date.today()
yesterday = (today - datetime.timedelta(days=1)).isoformat()
before_yesterday = (today - datetime.timedelta(days=2)).isoformat()

response = requests.get(STOCK_ENDPOINT, stock_parameters)
stock_data = response.json()["Time Series (Daily)"]

def calculate_price_change(data):
    y_price = float(data[yesterday]["4. close"])
    by_price = float(data[before_yesterday]["4. close"])

    price_change = round(((y_price - by_price) / by_price) * 100, 2)
    return price_change

change = calculate_price_change(stock_data)


NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "apiKey": NEWS_API,
    "sortBy": "popularity",
    "pageSize": 10
}
print(change)

if abs(change) >= 5:
    response = requests.get(NEWS_ENDPOINT, news_parameters)
    news_data = response.json()["articles"][:3]
    for article in news_data:
        print(article["description"])


## STEP 3: setup a telegram bot??


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

