"""

@Author Timothy
@Date 2nd May 2024

Dictionaries and APIs

"""

import requests

# Dictionaries
# Hold certain strings with values

supermarket = {
    "apple": 2,
    "banana": 3,
    "orange": 1,
}

print(supermarket["apple"])

person = {
    "name": "Timothy",
    "age": 22,
    "hobbies": ["Python", "Minecraft"],
}

# nested list
print(person["hobbies"][0])  # Python

classroom = {
    "teacher": {
        "name": "Timothy",
        "age": 22,
        "hobbies": ["Python", "Minecraft"],
    },
    "students": [
        {
            "name": "Luca",
            "age": 12,
            "hobbies": ["Python", "Destiny 2", "Taekwon-do"],
        },
        {
            "name": "Alkis",
            "age": 11,
            "hobbies": [],
        },
        {
            "name": "Cesar",
            "age": 10,
            "hobbies": [],
        },
    ],
}

# Task 1 - Print out Alkis' age
print(classroom["students"][1]["age"])

# helps us know what's inside a dictionary
print(classroom.keys())

# APIs
# a database of data
# linking information to an app
url = "http://numbersapi.com/random/math"
print(requests.get(url).text)
