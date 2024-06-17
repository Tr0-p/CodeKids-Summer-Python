"""

@Author: Timothy
@Date:  12th June 2024

APIs

"""

# QUICK REVIEW ON LISTS AND DICTIONARIES

# indexing lists
list_of_words = ["stand", "contract", "each", "using"]
# print(list_of_words[1])

# index dictionaries
dictionary_of_words = {
    "stand": 10,
    "contract": 3,
    "each": 5,
    "using": 2,
}
# print(dictionary_of_words["each"])

# import requests library
import requests

# our question we want to ask
url = "https://dogapi.dog/api/v2/facts"

# asking for a random dog fact
data = requests.get(url)
# print(data)  # we get "<Response [200]>"
# response 200: the question we asked, is received, and the data will come

# reading the response data as a dictionary / any python object
# can be lists or dictionaries

# convert our data in a python object
result = data.json()

# print out the data by indexing each layer
print(result["data"][0]["attributes"]["body"])

# write 5 dog facts into a text file
with open("dog_facts.txt", "w") as file:  # creates the text file
    for counter in range(0, 5):
        data = requests.get(url)
        result = data.json()
        fact = result["data"][0]["attributes"]["body"]
        file.write(f"{counter + 1}. {fact}\n")
