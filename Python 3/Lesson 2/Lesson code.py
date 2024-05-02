import random

# OLD VERSION:
"""
# def greet():
#     greetings = ["Hey there, how are you?", "Hi, I hope you're having a great day!", "Hello, very nice to meet you"]
#     return random.choice(greetings) # randomly picks a greeting from greetings list
#
# def goodbye():
#     goodbyes = ["Sad to see you go!", "Goodbye, see you later", "Nice talking, bye!"]
#     return random.choice(goodbyes)
"""


# NEW VERSION:
def message(message_type):
    messages = {"hello": ["Hey there, how are you?", "Hi, I hope you're having a great day!", "Hello, very nice to meet you"],
                "goodbye": ["Sad to see you go!", "Goodbye, see you later", "Nice talking, bye!"]}
    message = messages[message_type] # find the list of goodbyes/greetings depending on what we want
    return random.choice(message)


def respond(user_input):
    if user_input == "hello" or user_input == "goodbye":
        return message(user_input)
    else:
        return "Oops! I can't help you there (yet!)" # NEXT WEEK: use APIs to get weather forecast


user_input = input("Type here: ")
print(respond(user_input))