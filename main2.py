import re
import requests
import json

url1 = "http://numbersapi.com/random?json"

response1 = requests.get(url1)

if response1.status_code == 200:
    data1 = response1.json()
    print(f"Number Fact: {data1['text']}")  
else:
    print("Failed to retrieve a number fact.")