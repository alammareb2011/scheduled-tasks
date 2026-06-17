from http.client import responses
import os
from twilio.rest import Client

import requests


base_url = "https://api.openweathermap.org/"
five_days_Forecast_endpoint = "data/2.5/forecast"
parameters = {
    "lat": 9.533310,
    "lon": -10.957720,
    "appid": os.environ.get("OW_AKI_KEY"),
    "cnt": 4,
}
response = requests.get(url=f'{base_url}{five_days_Forecast_endpoint}', params=parameters)
response.raise_for_status()
weather = response.json()

weather_list = weather["list"]
from operator import index

will_rain = False
for n in weather_list:
    if weather_list.index(n) > 0 and n["weather"][0]["id"] < 700:
        if n["weather"][0]["id"] < 700:
            will_rain = True
if will_rain:
    print("pass")
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+14155238886",
        body="It's going to rain today. Remember to bring an umbrella",
        to="+966551676472"
    )

    print(message.status)
