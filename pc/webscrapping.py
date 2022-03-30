from bs4 import BeautifulSoup
import requests
import pandas as pd 

def search_gpu():
     userinput= input('Please Enter the name of the GPU: ')
     destenation ='https://www.newegg.com/p/pl?d='+userinput +'&N=100006662'

     html_text = requests.get(destenation).text
     soup= BeautifulSoup(html_text, 'lxml')
     items=soup.find_all('div', class_ = 'item-cell')

     
     for item in items:
          try:
               gpu = item.find('a', class_ ='item-title').text
               gpu_price = item.find('li', class_ ='price-current').text.split(" " ,0)[0].split("(")[0]
               
               with open('pc/data/gpu.csv','a') as f:
                    f.write(gpu+ '\n')
                    f.write(gpu_price+ '\n')
                    print(gpu)
                    print(gpu_price)
          except AttributeError:
               print("There is no such attribute")          


def search_cpu():
     user_input = input('Please Enter the name of the CPU: ')
     destenation = 'https://www.newegg.com/p/pl?d='+user_input+'&N=100006676'
     
     html_text = requests.get(destenation).text
     soup = BeautifulSoup(html_text, 'lxml')
     
     items = soup.find_all('div', class_ ='item-cell')
     
     for item in items:
          try:
               cpu = item.find('a', class_ = 'item-title').text
               cpu_price = item.find('li', class_='price-current').text.split(" ",0)[0].split("(")[0]
               
               with open('pc/data/cpu.csv','a') as f:
                    f.write(cpu+'\n')
                    f.write(cpu_price+'\n')
                    print(cpu)
                    print(cpu_price)
          except AttributeError:
               print("There is no such attribute")          
          
          
def search_ram():
     open('ram.csv','w').close()
     user_input = input('Please Enter the name of the RAM')
     destenation = 'https://www.newegg.com/p/pl?d='+user_input+'&N=100007611'

     html_text = requests.get(destenation).text
     soup = BeautifulSoup(html_text, 'lxml')
     
     items = soup.find_all('div', class_='item-cell')
     
     for item in items:
          try:
               ram = item.find('a', class_ = 'item-title').text
               ram_price = item.find('li', class_='price-current').text.split(" ",0)[0].split("(")[0]
               
               with open('pc/data/ram.csv','a') as f:
                    f.write(ram+'\n')
                    f.write(ram_price+'\n')
                    print(ram)
                    print(ram_price)
          except AttributeError:
               print("There is no such attribute")



def gpu_benchmark():
     open('pc/data/gpubenchmarks.csv','w').close()
     destenation = "https://benchmarks.ul.com/compare/best-gpus"
     user_input=input('Enter the GPU you want to find: ').upper()
     html_text=requests.get(destenation).text
     soup = BeautifulSoup(html_text,'lxml')
     items= soup.find_all('tr')

     for item in items:
          try:
            gpu_name=item.find('a',class_='OneLinkNoTx').text.strip()
            gpu_preformance=item.find('span',class_='bar-score').text.strip()
            with open('pc/data/gpubenchmarks.csv','a') as f:
               f.write(gpu_name+'  ') 
               f.write(gpu_preformance)
               f.write('\n')
               if user_input in gpu_name:
                    print(f'GPU: {gpu_name}   3DMARK Benchmark: {gpu_preformance}')
          
          except AttributeError:
               print('')
     
         
     
     
     
     
     
     
     
     
gpu_benchmark()