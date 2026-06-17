from http.client import responses
import os
from twilio.rest import Client

import requests

# print(os.environ)
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
# # print(weather)
weather_list = weather["list"]
from operator import index

# weather_dic = {'cod': '200', 'message': 0, 'cnt': 4, 'list': [{'dt': 1781438400, 'main': {'temp': 302.44, 'feels_like': 305.38, 'temp_min': 302.44, 'temp_max': 302.44, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 964, 'humidity': 64, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.36, 'deg': 282, 'gust': 0.88}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2026-06-14 12:00:00'}, {'dt': 1781449200, 'main': {'temp': 301.84, 'feels_like': 305.04, 'temp_min': 300.64, 'temp_max': 301.84, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 962, 'humidity': 69, 'temp_kf': 1.2}, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.89, 'deg': 105, 'gust': 3.12}, 'visibility': 10000, 'pop': 0.99, 'rain': {'3h': 5.99}, 'sys': {'pod': 'd'}, 'dt_txt': '2026-06-14 15:00:00'}, {'dt': 1781460000, 'main': {'temp': 300.27, 'feels_like': 303.16, 'temp_min': 299.18, 'temp_max': 300.27, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 962, 'humidity': 80, 'temp_kf': 1.09}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.53, 'deg': 164, 'gust': 2.78}, 'visibility': 10000, 'pop': 0.99, 'rain': {'3h': 2.37}, 'sys': {'pod': 'd'}, 'dt_txt': '2026-06-14 18:00:00'}, {'dt': 1781470800, 'main': {'temp': 296.22, 'feels_like': 297.01, 'temp_min': 296.22, 'temp_max': 296.22, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 964, 'humidity': 93, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 98}, 'wind': {'speed': 1.76, 'deg': 215, 'gust': 2.68}, 'visibility': 10000, 'pop': 0.72, 'rain': {'3h': 0.62}, 'sys': {'pod': 'n'}, 'dt_txt': '2026-06-14 21:00:00'}], 'city': {'id': 2409019, 'name': 'Gberia Fotombu', 'coord': {'lat': 9.5333, 'lon': -10.9577}, 'country': 'SL', 'population': 3034, 'timezone': 0, 'sunrise': 1781418234, 'sunset': 1781463862}}
# weather_list = weather_dic["list"]
# print(weather_list)
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
# actual_weather = {}
# for n in weather_list:
#     # print(n["weather"][0])
#     actual_weather[n] = n["weather"][0]

# print(actual_weather)
# print(actual_weather)
# def is_it_raining():
#     w