# We start by importing the requests library.
# This library helps us send requests to websites and get information back.
import requests

# This function takes a country name as input and returns its population.
def get_population(country_name):
    # Here we construct the URL for the API.
    # We put the country name in the URL to get data specifically for that country.
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    # Now, we send a GET request to the URL to get information about the country.
    response = requests.get(url)
    
    # We check if the request was successful (status code 200 means success).
    if response.status_code == 200:
        # If successful, we get the data from the response in JSON format.
        data = response.json()
        
        # If the data is not empty (meaning the country exists),
        if data:
            # We extract the information about the country.
            country_data = data[0]
            
            # If the population information is available for the country,
            if 'population' in country_data:
                # We return the population.
                return country_data['population']
            else:
                # If population information is not available, we return this message.
                return "Population data not available for this country."
        else:
            # If the country is not found, we return this message.
            return "Country not found."
    else:
        # If the request failed, we return this message.
        return "Failed to fetch data."

# This is the main part of our script.
if __name__ == "__main__":
    # We ask the user to input the name of the country they want to know about.
    country_name = input("Enter the name of the country: ")
    
    # We call the get_population function with the country name provided by the user.
    # This function returns the population of the country (if available).
    population = get_population(country_name)
    
    # Finally, we print the population of the country (or any message if it's not available).
    print(f"Population of {country_name}: {population}")
