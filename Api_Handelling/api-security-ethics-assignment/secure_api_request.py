import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("key")
url = "https://covid-19-statistics.p.rapidapi.com/regions"

headers = {
	"x-rapidapi-key": api_key,
	"x-rapidapi-host": "covid-19-statistics.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code==200:
    print(response.json())
elif response.status_code==429:
    print("Rate limit reached. Try again later.")
else:
    print("Request Failed")



