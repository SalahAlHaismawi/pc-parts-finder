from bs4 import BeautifulSoup
import requests

def search_gpu():
     userinput= input('Please Enter the name of the GPU: ')
     destenation ='https://www.newegg.com/p/pl?d='+userinput +'&N=100006662'

     html_text = requests.get(destenation).text
     soup= BeautifulSoup(html_text, 'lxml')
     items=soup.find_all('div', class_ = 'item-cell')

     
     for item in items:
          gpu = item.find('a', class_ ='item-title').text
          gpu_price = item.find('li', class_ ='price-current').text.split(" ",0)[0].split("(")[0]
          
          with open('gpu.csv','a') as f:
               f.write(gpu+'/n')
               f.write(gpu_price+'\n')
               print(gpu+'/n')
               print(gpu_price+'\n')
              