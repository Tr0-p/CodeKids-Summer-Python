"""
@Author: Timothy
@Date: 26th June 2024

Pokemon APIs
"""

import requests

search = input("What Pokemon do you want to look up? ")
search = search.lower()
api = f"https://pokeapi.co/api/v2/pokemon/{search}/"

try:
    result = requests.get(api).json()
    # print(result.keys())
    print(f"Height: {result['height']}")
    print(f"Weight: {result['weight']}")
    print(f"Type: {result['types'][0]['type']['name']}")
    print(f"Move: {result['moves'][0]['move']['name']}")

    with open(f"{search}.txt", "w") as w:
        w.write(f"{search.upper()}\n\n")
        w.write("----- Stats -----\n")
        w.write(f"Height: {result['height']}\n")
        w.write(f"Weight: {result['weight']}\n")
        w.write(f"Type: {result['types'][0]['type']['name']}\n")
        w.write(f"Move: {result['moves'][0]['move']['name']}\n")

except:
    print(f"No such pokemon - {search}")
