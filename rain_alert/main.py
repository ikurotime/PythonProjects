import requests
import os
from twilio.rest import Client

api_key = 'acb606d14dc803b10a0825c3e81d62a2'
URL = 'https://api.openweathermap.org/data/2.5/onecall'
SID = 'AC3af6b2c0ce45cbbb82445600873441b4'
account_sid = 'AC3af6b2c0ce45cbbb82445600873441b4'
auth_token = '33d94057212fb892f64688227e92984d'

weather_parameters = {
    'exclude':'daily,minutely,current',
    'lat': 40.4165,
    'lon': -3.7026,
    'appid': api_key
}
response = requests.get(url = URL, params = weather_parameters)
data_weather = response.json()
slice = data_weather['hourly'][:12]
will_rain = False
for hour in range(0,12):
    forecast = slice[hour]['weather'][0]['id']
    if forecast < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body = "It's going to rain today. Remember to bring an ☂️️️!",
            from_ = '+18186965682',
            to = '+34674268546'
    )
    print(message.status)