# Q11. Web Scraping Task: (5 Marks)
# • Scrape this website: http://quotes.toscrape.com
# • Get all quotes and authors
# • Print only quotes by 'Albert Einstein'
# • Save ALL quotes to 'quotes.json'
# • Print total number of quotes scraped

import requests
from bs4 import BeautifulSoup
import json

url="http://quotes.toscrape.com/"
response=requests.get(url)
soap=BeautifulSoup(response.text,"html.parser")

qoutes=soap.find_all('span',class_="text")
authors=soap.find_all('small',class_="author")

data=[]
for quote,author in zip(qoutes,authors):
    if(author.text=='Albert Einstein'):
        print(quote.text)
    data.append({
        'quote':quote.text,
        'author':author.text
    }) 


with open('quotes.json','w') as f:
    json.dump(data,f,indent=4)

print("Data Saved")