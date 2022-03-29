from bs4 import BeautifulSoup
import requests
userinput='3060'
destenation ='https://www.newegg.com/p/pl?d='+userinput
print(destenation)
html_text = requests.get(destenation).text
soup= BeautifulSoup(html_text, 'lxml')
gpu= soup.find_all('strong', class_='price-current')
print(gpu)