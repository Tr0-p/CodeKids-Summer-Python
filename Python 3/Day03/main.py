"""

@Author Timothy
@Date 9th May 2024

APIs

"""

# take data from third party
# use in our own environment / program

import requests

math_url = "http://numbersapi.com/random/math"

# print(requests.get(math_url).text)

activity_url = "https://www.boredapi.com/api/activity/"

# JSON
# JavaScript Object Notation
# response = requests.get(activity_url).json()
# print(type(response))
# print(response["activity"])

word = input("What word would you like to define? ")

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

response = requests.get(url).json()
# print(response) => will be a wall of info

# trick no.1
# get the type of the response we are seeing
# print(type(response))

# trick no.2
# if we get a list, use the first element to deal with the details
# print(response[0])
# print(type(response[0]))

# trick no.3
# if we get a dictionary, use .keys() and see which key is relevant
# print(response[0].keys())

print(response[0]["meanings"][0]["definitions"][0]["definition"])
