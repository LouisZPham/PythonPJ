#install pandas, numby, pytz
import pandas
import requests
from bs4 import BeautifulSoup

url = 'https://www.latex-project.org/latex3/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.string
text = soup.get_text()
words = text.split()

print(title)
print(words)
print(" ".join(words))
###
data = pandas.read_csv("https://www.latex-project.org/latex3/", encoding='utf-8')
#The parser error occured. 
print(data.head())
###
