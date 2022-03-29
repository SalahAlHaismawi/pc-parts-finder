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
               f.write(gpu+'\n')
               f.write(gpu_price+'\n')
               print(gpu)
               print(gpu_price)


def search_cpu():
     user_input = input('Please Enter the name of the CPU: ')
     destenation = 'https://www.newegg.com/p/pl?d='+user_input+'&N=100006676'
     
     html_text = requests.get(destenation).text
     soup = BeautifulSoup(html_text, 'lxml')
     
     items = soup.find_all('div', class_ ='item-cell')
     
     for item in items:
          cpu = item.find('a', class_ = 'item-title').text
          cpu_price = item.find('li', class_='price-current').text.split(" ",0)[0].split("(")[0]
          
          with open('cpu.csv','a') as f:
               f.write(cpu+'\n')
               f.write(cpu_price+'\n')
               print(cpu)
               print(cpu_price)
          
          
def search_ram():
     user_input = input('Please Enter the name of the RAM')
     destenation = 'https://www.newegg.com/p/pl?d='+user_input+'&N=100007611'

     html_text = requests.get(destenation).text
     soup = BeautifulSoup(html_text, 'lxml')
     
     items = soup.find_all('div', class_='item-cell')
     
     for item in items:
           ram = item.find('a', class_ = 'item-title').text
           ram_price = item.find('li', class_='price-current').text.split(" ",0)[0].split("(")[0]
          
           with open('ram.csv','a') as f:
               f.write(ram+'\n')
               f.write(ram_price+'\n')
               print(ram)
               print(ram_price)


search_ram()
