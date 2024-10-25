import requests
from dotenv import load_dotenv
import os
load_dotenv()

API = os.getenv('API_KEY')





def get_top_news(country, api=API):
  url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api}"
  res = requests.get(url)
  content = res.json()
  # print(content)
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"Title:\n {article['title']}\nDesc:\n{article['description']}\n\n")
  return results


print(get_top_news(country="us"  ))
print(get_top_news(country="us" )[0])
