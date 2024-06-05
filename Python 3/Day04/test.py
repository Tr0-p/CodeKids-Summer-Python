import webbrowser as wo

import PySimpleGUI as sg
import requests as r


def main():
    ip = "https://api.aruljohn.com/ip/json"
    responseip = r.get(ip).json()
    bored = "https://www.boredapi.com/api/activity"
    urldog = "https://dog.ceo/api/breeds/image/random"
    loc = f"https://api.country.is/{responseip['ip']}"
    joke = "https://v2.jokeapi.dev/joke/Any?safe-mode"
    fox = "https://randomfox.ca/floof/"
    cat = "https://yesno.wtf/api"
    responsefox = r.get(fox).json()
    responsedog = r.get(urldog).json()
    responseloc = r.get(loc).json()
    responsejoke = r.get(joke).json()
    # responsebored = r.get(bored).json()
    responsecat = r.get(cat).json()

    def welcome():
        return [
            [sg.Text("Welcome to the API Aplication")],
            [sg.Button("Next")],
            [sg.Button("Quit")],
        ]

    def choose():
        return [
            [sg.Text("Choose One of the APIs")],
            [sg.Button("IP Address", key="ip")],
            [sg.Button("Boredapi Activity Finder", key="bored")],
            [sg.Button("Age Guessing Based on name", key="age")],
            [sg.Button("Random Dog Breed Photo", key="dog")],
            [sg.Button("Geolocation from IP address", key="l")],
            [sg.Button("Joke", key="j")],
            [sg.Button("Fox Images", key="f")],
            [sg.Button("Yes or No gif ", key="c")],
        ]

    def ip():
        return [[sg.Text(f"Your IP Address Is {responseip['ip']}")]]

    def bored():
        return [[sg.Text(responsebored["activity"])]]

    def age1():
        return [[sg.Input("Input your Name", key="age_input")], [sg.Button("Next")]]

    def age2():
        return [[sg.Text(f"Guessed age: {responseage['age']}")]]

    def dog():
        return [[sg.Button("Show Photo")]]

    def loc():
        return [[sg.Text(responseloc["country"])]]

    def joke():
        return [[sg.Text(responsejoke["setup"])], [sg.Text(responsejoke["delivery"])]]

    def fox():
        return [[sg.Button("Show Photo")]]

    def cat():
        return [[sg.Button("Show Photo")]]

    welcome = sg.Window("APIs", welcome())
    while True:
        events, values = welcome.read()
        if events == "Quit":
            welcome.close()
            break
        if events == sg.WIN_CLOSED:
            welcome.close()
            break
        if events == "Next":
            welcome.close()
            choose = sg.Window("APIs", choose())
            while True:
                events, values = choose.read()
                if events == sg.WIN_CLOSED:
                    choose.close()
                    break
                if events == "ip":
                    choose.close()
                    ip = sg.Window("APIs", ip())
                    while True:
                        events, values = ip.read()
                        if events == sg.WIN_CLOSED:
                            ip.close()
                            break
                if events == "bored":
                    choose.close()
                    bored = sg.Window("APIs", bored())
                    while True:
                        events, values = bored.read()
                        if events == sg.WIN_CLOSED:
                            bored.close()
                            break
                if events == "age":
                    choose.close()
                    age1 = sg.Window("APIs", age1())
                    while True:
                        events, values = age1.read()
                        if events == sg.WIN_CLOSED:
                            age1.close()
                            break
                        if events == "Next":
                            age1.close()
                            name = values["age_input"]
                            ageguess = f"https://api.agify.io/?name={name}"
                            responseage = r.get(ageguess).json()
                            age2 = sg.Window("APIs", age2())
                            while True:
                                events, values = age2.read()
                                if events == sg.WIN_CLOSED:
                                    age2.close()
                                    break
                if events == "dog":
                    choose.close()
                    dog = sg.Window("APIs", dog())
                    while True:
                        events, values = dog.read()
                        if events == sg.WIN_CLOSED:
                            dog.close()
                            break
                        if events == "Show Photo":
                            wo.open_new_tab(responsedog["message"])
                if events == "l":
                    choose.close()
                    loc = sg.Window("APIs", loc())
                    while True:
                        events, values = loc.read()
                        if events == sg.WIN_CLOSED:
                            loc.close()
                            break
                if events == "j":
                    choose.close()
                    joke = sg.Window("APIs", joke())
                    while True:
                        events, values = joke.read()
                        if events == sg.WIN_CLOSED:
                            joke.close()
                            break
                if events == "f":
                    choose.close()
                    fox = sg.Window("APIs", fox())
                    while True:
                        events, values = fox.read()
                        if events == sg.WIN_CLOSED:
                            fox.close()
                            break
                        if events == "Show Photo":
                            wo.open_new_tab(responsefox["image"])
                if events == "c":
                    choose.close()
                    cat = sg.Window("APIs", cat())
                    while True:
                        events, values = cat.read()
                        if events == sg.WIN_CLOSED:
                            cat.close()
                            break
                        if events == "Show Photo":
                            wo.open(responsecat["image"])


main()
