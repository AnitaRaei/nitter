#5 top tweets from below url
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://nitter.net/shywn_mrk'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

tweets = soup.find_all('div', attrs={'class':'tweet-content media-body'})

tweet = []

for i in range(5):
    tweet.append(tweets[i].text)

data = {'Tweets':tweet}

df = pd.DataFrame(data)

writer = pd.ExcelWriter('nitter.xlsx')
df.to_excel(writer,'sheet1')
writer.save()

