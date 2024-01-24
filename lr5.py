import requests

def get_weather(city_name):
    api_key = "d57fbcd493b4b09809f8f7ed73d7a7f9"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city_name,
        'appid': api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']

        print(f"Weather in {city_name}: {weather_description}")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
    else:
        print(f"Error: {data['message']}")

city_name = input("Введите название города: ")
get_weather(city_name)
