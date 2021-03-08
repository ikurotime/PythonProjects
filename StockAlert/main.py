import requests
import os
from twilio.rest import Client
from datetime import *

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc'
STOCK_API_KEY = 'VKA2WQHQMJKW7ZO0'
NEWS_API_KEY = '9e9c659492b54def94acbe2829703b96'
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

account_sid = 'AC3af6b2c0ce45cbbb82445600873441b4'
auth_token = '33d94057212fb892f64688227e92984d'

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}
news_parameters = {
    'q': COMPANY_NAME,
    'from': '2021-03-04',
    # 'sortBy': 'date',
    'apiKey': NEWS_API_KEY
}


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0


stock_json = requests.get(url = STOCK_ENDPOINT, params = stock_parameters)
stock_data = stock_json.json()

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]
yesterday = datetime.today().date() - timedelta(days = 1)
yesterday_date = str(yesterday)
bf_yesterday = datetime.today().date() - timedelta(days = 2)
bf_yesterday_date = str(bf_yesterday)

ystday_closing_stock_data = float(stock_data['Time Series (Daily)'][yesterday_date]['4. close'])

# TODO 2. - Get the day before yesterday's closing stock price
bf_ystday_closing_stock_data = float(stock_data['Time Series (Daily)'][bf_yesterday_date]['4. close'])

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = (abs(ystday_closing_stock_data - bf_ystday_closing_stock_data))
up_down = None
if ystday_closing_stock_data - bf_ystday_closing_stock_data > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(f'positive diff: {positive_difference}')

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
percent_diff = get_change(ystday_closing_stock_data, bf_ystday_closing_stock_data)
print(f'% diff: {round(percent_diff, 2)}')

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_diff >= 4:
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(url = NEWS_ENDPOINT, params = news_parameters)
    news_json = news_response.json()

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint:
    #  https://stackoverflow.com/questions/509211/understanding-slice-notation
    if len(news_json) > 3:
        news_pieces = news_json['articles'][:3]
    else:
        news_pieces = news_json['articles']
    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    news_articles = [
        f"{STOCK_NAME}: {up_down}{round(percent_diff, 2)}%\n"
        f"Headline: {news_pieces[num]['title']}\n"
        f"Brief: {news_pieces[num]['description']}"
        for num in range(3)]
    print(news_articles[0])
    # TODO 9. - Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)

    message_1 = client.messages \
        .create(
            body = f"{news_articles[0]}",
            from_ = '+18186965682',
            to = '+34674268546'
                )
    message_2 = client.messages \
        .create(
            body = f"{news_articles[1]}",
            from_ = '+18186965682',
            to = '+34674268546'
                )
    message_3 = client.messages \
        .create(
            body = f"{news_articles[2]}",
            from_ = '+18186965682',
            to = '+34674268546'
                )
