import requests

# i have made them download the request module already
# so this should work for everyone

# warm up activity
# should take around 10 - 15 minutes
# an activity api to get suggests for what to do when bored
url = "https://bored-api.appbrewery.com/random"

res = requests.get(url).json()

# first step to check the keys of the response
# see which category is most relevant to us
print(res.keys())

# print out the data we want to display
print(f"Activity: {res['activity']}")
if res["kidFriendly"]:
    print(f"Kid Friendly: True")
else:
    print(f"Kid Friendly: False")

# open a new file for this weather app

# you can ask them how do we get python to ask us a question
location = input("Where is your destination? ")

# send this to the student, I will void the apikey after wednesday
key = "PMLqlxdwNuJzLxVqItMYL12mTpUomn9p"
url = f"https://api.tomorrow.io/v4/weather/forecast?location={location}&apikey={key}"

# getting our response and turning it into a dictionary
res = requests.get(url).json()

# first step to check the keys of the response
# see which category is most relevant to us
# repeat until we see something we like
# print(res.keys())
# print(res["timelines"].keys())
# ...

items = res["timelines"]["daily"]
# you can ask them how can we loop over the items in the list
for i in range(0, len(items)):
    item = items[i]
    time = item["time"]
    # you can teach them slicing substrings if there is time
    # this only makes things look nicer
    # time = item["time"][:10]
    minTemp = item["values"]["temperatureMin"]
    maxTemp = item["values"]["temperatureMax"]

    print(f"On {time} temperature ranges from {minTemp} to {maxTemp}")
    print("---")
