# -*- coding: utf-8 -*-

from time import sleep

import requests

city = 'Геленджик'

url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + \
      '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'


def weather():
    weather_data = requests.get(url).json()

    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    wind_speed = weather_data['wind']['speed']

    print(f'Сейчас в городе, {city}, {str(temperature)}°C')
    print(f'Ощущается как, {str(temperature_feels)}°C')
    print('Скорость ветра', str(wind_speed), 'м/с')

    return [city + str(temperature) + " °C", "Ощущается как, " + str(temperature_feels) + " °C",
            "Скорость ветра, " + str(wind_speed) + " м/с"]


weather()
