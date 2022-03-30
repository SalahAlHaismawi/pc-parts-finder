from numpy import mat
from webscrapping import *

def show_gpu_menu():
    print(
        "------------------------------------------------------\n"
       +"|                |Graphics Card Menu|                |\n"
       +"|----------------------------------------------------|\n"
       +"|1-Check a specific Graphic Card benchmarks:         |\n"
       +"|----------------------------------------------------|\n"
       +"|2-Check a specific Graphic Card price               |\n"
       +"|----------------------------------------------------|\n"
    )
    ch=input()
    def f(ch):
        match ch:
            case '1': gpu_benchmark()
            case '2': search_gpu()          
    
    f(ch)
    
            