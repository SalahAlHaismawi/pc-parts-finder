from bs4 import BeautifulSoup
import requests
userinput='3060'
destenation ='https://www.newegg.com/p/pl?d='+userinput
print(destenation)
html_text = requests.get(destenation).text
soup= BeautifulSoup(html_text, 'lxml')
item_cell=soup.find('div',class_='item-cell')

gpu=item_cell.find('a',class_='item-title').text
gpu_price=item_cell.find('li',class_='price-current').text.split(" ",0)[0].split("(")[0]

print(gpu)
print(gpu_price)