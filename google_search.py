import urllib
import requests
import time
from bs4 import BeautifulSoup
import csv

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
query = 'Python'
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}&num=20"

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='rc'):
        anchors = g.find_all('a')
        spans=g.find_all('span')
        if anchors:
          title = g.find('h3').text
          link = anchors[0]['href']
        if spans:
          span=spans[-1].text 
        results.append([title,link,span])

    
with open('data.csv','w') as fp:
  wr=csv.writer(fp)
  wr.writerows(results)
