import json

import requests

city = 'Геленджик'

url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + \
      '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'


def weather():
    weather_data = requests.get(url).json()
    weather_data_structure = json.dumps(weather_data, indent=2, ensure_ascii=False)

    temperature = round(weather_data["main"]["temp"])
    temperature_feels = round(weather_data["main"]["feels_like"])
    wind_speed = weather_data["wind"]["speed"]
    weather_description = weather_data["weather"][0]["description"]
    air_humidity = weather_data["main"]["humidity"]

    return [f"{city} {str(temperature)} °C", f"Ощущается как {str(temperature_feels)} °C",
            f"Скорость ветра {str(wind_speed)} м/с", weather_description.capitalize(),
            f"Влажность воздуха {air_humidity} %"]
