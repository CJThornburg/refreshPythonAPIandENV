import requests
from dotenv import load_dotenv
import os
load_dotenv()

API = os.getenv('API_KEY')

res = requests.get(f"https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-9-27&to=2022-2-28&sortBy=popularity&language=en&apiKey={API}")


content = res.json()
print(type(content))
print(content["articles"][0]['title'])
print(content["articles"][0]['description'])
print(content["articles"][0]["content"])
