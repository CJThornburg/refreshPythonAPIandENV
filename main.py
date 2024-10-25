import requests
from dotenv import load_dotenv
import os
load_dotenv()

API = os.getenv('API_KEY')





def get_news(topic,from_date, to_date, language="en", api=API):
  url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api}"
  res = requests.get(url)
  content = res.json()
  # print(content)
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"Title:\n {article['title']}\nDesc:\n{article['description']}\n\n")
  return results


print(get_news(topic="space", from_date="2024-10-07", to_date="2024-10-20" ))
print(get_news(topic="space", from_date="2024-10-07", to_date="2024-10-20" )[0])
