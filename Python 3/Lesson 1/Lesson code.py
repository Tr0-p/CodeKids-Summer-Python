import requests


# MESSY CODE

## How would you make it more structured?
## Functions? Lists or Dictionaries to store data?

response = requests.get('https://api.spacexdata.com/v3/launches/upcoming')
stuff = response.json() # Poor variable name
print(stuff)
print(stuff[0]['mission_name']),
print(list(stuff[0].values())[4]) # Just printing the value without the key - don't know what the value is referring
x = stuff[0]['launch_site']
long = x['site_name_long']
print(long)
print('todo') # Strange way to record that the code is incomplete
# Meaningless/confusing names for our variables
thing = stuff[0]['rocket']
thing2 = thing['second_stage']
thing3 = thing2['payloads']
thing4 = thing3[0]
print(thing4['payload_type'])

# Inefficient way to add line breaks:
print("")
print("")
print("")



# CLEAN CODE

# 1. Uses functions
# 2. Uses sensible variable names
# 3. Uses appropriate data structures (dictionary) where needed

def get_data(url):
    response = requests.get(url) # make a request to the api
    data = response.json() # get the json information
    return data # send back the json data

upcoming_launch_url = 'https://api.spacexdata.com/v3/launches/upcoming'
upcoming_launch_data = get_data(upcoming_launch_url)


launch_data = {
    "Mission": upcoming_launch_data[0]['mission_name'],
    "Launch year": upcoming_launch_data[0]['launch_year']
}

print(launch_data)
