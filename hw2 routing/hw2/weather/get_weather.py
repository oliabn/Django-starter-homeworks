import requests
import json
from .tokens import WEATHER_TOKEN


WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> dict:
    """Return dict with data about weather from website OpenWeather"""

    # Sending request and Getting response
    params = {"q": f"{city}", "appid": WEATHER_TOKEN, "units": "metric"}
    response = requests.get(WEATHER_URL, params=params)
    data = json.loads(response.content)
    return parse_weather_data(data, response.status_code, city)


def parse_weather_data(data: dict, status: int, city: str) -> dict:
    """Parses a dict of weather data obtained from the site OpenWeather
     and forms a dictionary with the necessary information."""
    if status != 200:
        print(status)
        weather_data = {
            'country': None,
            'city': f'<{city}> city does not exist!',
            'lon': None,
            'lat': None,
            'weather': None,
            'temperature': None,
        }
    else:
        weather_data = {
            'country': data['sys']['country'],
            'city': data['name'],
            'lon': data['coord']['lon'],
            'lat': data['coord']['lat'],
            'weather': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
        }
    return weather_data


# Test get_weather()
if __name__ == "__main__":
    for data in get_weather('Lodz').items():
        print(data)
