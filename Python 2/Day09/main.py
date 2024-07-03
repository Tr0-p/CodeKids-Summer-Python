"""
@Author: Timothy
@Date: 26th June 2024

Pokemon APIs
"""

import requests

search = input("What Pokemon do you want to look up? ")
search = search.lower()
api = f"https://pokeapi.co/api/v2/pokemon/{search}/"

# try:
result = requests.get(api).json()
print(result.keys())
print(f"Height: {result['height']}")
print(f"Weight: {result['weight']}")
print(f"Type: {result['types'][0]['type']['name']}")
print(result["moves"][0]["move"]["name"])

# add 3 - 4 more statistics of the pokemon

# except:
# print(f"No such pokemon - {search}")
