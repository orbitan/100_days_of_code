import requests
from datetime import date

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API = "SO9JJZGXPI2F1NC4"
ALPHA_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={ALPHA_API}"
TODAY = date.today()

NEWS_API = "2245ed5999b04048aaa4904e82677151"
NEWS_URL = f"https://newsapi.org/v2/everything?q={STOCK}&from={TODAY}&sortBy=popularity&apiKey={NEWS_API}"


#  Send a request
def request(url):
    r = requests.get(url)
    data = r.json()
    return data



data = request(ALPHA_URL)
stock_daily_result = data["Time Series (Daily)"]

today = str(date.today())

todays_day = today[len(today) - 2:]
yesterday = today.replace(f"{todays_day}", f"{(int(todays_day) - 1)}".zfill(2))
day_before_yesterday = today.replace(f"{todays_day}", f"{(int(todays_day) - 2)}".zfill(2))

stock_status_yesterday = stock_daily_result[yesterday]["1. open"].replace(".", "")
stock_status_day_before_yesterday = stock_daily_result[day_before_yesterday]["1. open"].replace(".", "")


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#
def comparison(yesterday, day_before_yesterday):
    yesterday = int(yesterday)
    day_before_yesterday = int(day_before_yesterday)

    absolute_difference = yesterday - day_before_yesterday
    if absolute_difference < 0:
        absolute_difference = absolute_difference * (-1)
    percentage = (absolute_difference / ((yesterday + day_before_yesterday) / 2)) * 100
    if percentage > 1:
        get_news()


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news():
    data = request(NEWS_URL)
    for i in range(3):
        article_des = data["articles"][i]['title'] + ":", data["articles"][i]['description']
        send_sms(article_des)


comparison(stock_status_yesterday, stock_status_day_before_yesterday)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_sms(article):
    pass


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
