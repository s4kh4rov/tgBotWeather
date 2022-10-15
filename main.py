import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):

    code_to_smile ={
         "Clear": "Ясно \U00002600 ",
         "Clouds": "Облачно \U00002601 ",
         "Rain":"Дождь \U00002614 ",
         "Thunderstorm":"Гроза \U000026A1",
         "Snow":"Снег \U0001F328"
    }

    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + open_weather_token + "&units=metric"
        r = requests.get(url)
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[ weather_description]
        else:
            wd = "Посмотри в окно,не могу понять что там за погода"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        weather_result_info = f"Погода в городе {city}\n Температура {cur_weather} °С {wd}\n Влажность {humidity} % \n Давление {pressure} мм.рт.ст \n Ветер {wind} м/с\n Восход солнца {sunrise_timestamp}\n Закат солнца {sunset_timestamp}\n Продолжительность светового дня  {lenght_of_the_day} \n Удачного дня!"

        print(weather_result_info)
    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input("Введите нужный город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
