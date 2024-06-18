import requests
import json

# Replace with your OpenWeatherMap API key
API_KEY = '2a151f417804bccb8fb2da543cea291f'

def get_data(city):
    """
    Retrieve weather data for a given city from OpenWeatherMap.

    Parameters:
    city (str): The name of the city.

    Returns:
    dict: The retrieved weather data as a dictionary.
    """
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Units in Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_weather(data):
    """
    Display weather data from OpenWeatherMap.

    Parameters:
    data (dict): The weather data to display.

    Returns:
    None
    """
    if data:
        print(f"City: {data['name']}")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("No data available.")

if __name__ == "__main__":
    city = input("Which city shall we get the weather for? ")
    weather_data = get_data(city)

    if weather_data:
        display_weather(weather_data)
    else:
        print("Sorry, weather data is not available for that city.")
