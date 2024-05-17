import random
import requests

base_url = "https://api.open-meteo.com/v1/"

def get_weather(latitude, longitude, weather):
    response = requests.get(f"{base_url}forecast?latitude={latitude}&longitude={longitude}&current={weather}")
    result = response.json()
    return str(result["current"][weather])+result["current_units"][weather]


def message(message_type):
    messages = {"hello": ["Hey there, how are you?", "Hi, I hope you're having a great day!", "Hello, very nice to meet you"],
                "goodbye": ["Sad to see you go!", "Goodbye, see you later", "Nice talking, bye!"]}
    message = messages[message_type] # find the list of goodbyes/greetings depending on what we want
    return random.choice(message)

def respond(user_input):
    if user_input == "hello" or user_input == "goodbye":
        return message(user_input)
    elif user_input == "temperature":
        latitude = input("What is the latitude? ")
        longitude = input("What is the longitude? ")
        return get_weather(latitude, longitude, 'temperature_2m')
    elif user_input == "wind":
        latitude = input("What is the latitude? ")
        longitude = input("What is the longitude? ")
        return get_weather(latitude, longitude, 'wind_speed_10m')
    else:
        return "Oops! I can't help you there (yet!)"

user_input = input("What would you like to do (hello/goodbye/temperature/wind): ")
print(respond(user_input))
