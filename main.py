import requests

# Joke API endpoint

url = "https://official-joke-api.appspot.com/random_joke"


# Send GET request to fetch a joke

response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    joke = response.json() 
    print(f"{joke['setup']} - {joke['punchline']}")
else:
    print("Failed to retrieve a joke.")

# https://github.com/skillacademyonwheels/1.-GettingStarted-with-API.git