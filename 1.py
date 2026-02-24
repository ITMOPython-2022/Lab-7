import requests
import sys

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        
    def get_weather(self, city_name):
        try:
            params = {
                'q': city_name,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'ru'
            }
            
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Проверка на ошибки HTTP
            
            data = response.json()
            return self._format_weather_data(data)
            
        except requests.exceptions.RequestException as e:
            return f"Ошибка при запросе к API: {str(e)}"
        except KeyError:
            return "Ошибка: неверный формат данных от API"
        except Exception as e:
            return f"Неизвестная ошибка: {str(e)}"
    
    def _format_weather_data(self, data):
        weather_info = {
            "Город": data.get('name', 'Н/Д'),
            "Погодные условия": data['weather'][0]['description'].capitalize(),
            "Температура": f"{data['main']['temp']}°C",
            "Ощущается как": f"{data['main']['feels_like']}°C",
            "Влажность": f"{data['main']['humidity']}%",
            "Давление": f"{data['main']['pressure']} гПа",
            "Ветер": f"{data['wind']['speed']} м/с",
            "Видимость": f"{data.get('visibility', 'Н/Д')} м"
        }
        
        formatted_output = "\n".join([f"{key}: {value}" for key, value in weather_info.items()])
        return formatted_output

def main():
    # Ваш API-ключ (в реальном проекте лучше хранить в переменных окружения)
    API_KEY = "38334ac1317f3a46fc0373a033abfdb0"
    
    app = WeatherApp(API_KEY)
    
    print("Программа для получения данных о погоде")
    print("Для выхода введите 'выход' или 'exit'\n")
    
    while True:
        city = input("Введите название города: ").strip()
        
        if city.lower() in ('выход', 'exit'):
            print("Программа завершена.")
            sys.exit(0)
            
        if not city:
            print("Ошибка: название города не может быть пустым")
            continue
            
        weather_data = app.get_weather(city)
        print(f"\n{weather_data}\n")

if __name__ == "__main__":
    main()
