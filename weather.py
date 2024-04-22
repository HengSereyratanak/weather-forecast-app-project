import requests
from timezonefinder import TimezoneFinder
from datetime import datetime
from pytz import timezone

def get_weather(city):
    try:
        obj = TimezoneFinder()

        # Weather API
        api_key = 'a0aff41729c3c32ac41798b2a6e9aabb'
        endpoint = "http://api.openweathermap.org/data/2.5/weather"
        params_data = {
            "appid": api_key,
            "q": city,
            "units": "metric"
        }

        data = requests.get(f'{endpoint}', params=params_data).json()

        condition = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = int(data['main']['temp'])
        feel_like = int(data['main']['feels_like'])
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        user_timezone = obj.timezone_at(lng=data["coord"]["lon"], lat=data["coord"]["lat"])
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"], tz=timezone(user_timezone)).strftime("%I:%M:%p")
        sunset = datetime.fromtimestamp(data["sys"]["sunset"], tz=timezone(user_timezone)).strftime("%I:%M:%p")

        current_time = datetime.now(timezone(user_timezone)).strftime("%I:%M:%S %p")

        return {
            "condition": condition,
            "description": description,
            "temp": temp,
            "feel_like": feel_like,
            "pressure": pressure,
            "humidity": humidity,
            "wind": wind,
            "sunrise": sunrise,
            "sunset": sunset,
            "current_time": current_time
        }
    except Exception as e:
        return None