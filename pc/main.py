from gpu import *
from webscrapping import *
from ram import *
from webscrapping import *
from cpu import *
import sys
sys.tracebacklimit=0
def starting_menu():
    print(
        "|----------------------------------------------------------------------|\n"
       +"|             THIS PROGRAM WAS MADE BY SALAH ALHAISMAWI                |\n"
       +"|----------------------------------------------------------------------|\n"
       +"|1-To view Graphic cards and thier benchmarks.                         |\n" 
       +"|2-To view CPU's and thier benchmarks.                                 |\n"
       +"|3-To view RAM Models.                                                 |\n"
       +"|4-To Choose a recommended psu depending on your need.                 |\n"
       +"|----------------------------------------------------------------------|\n"    
    )
    
    ch = input()
    
    def f(ch):
        match ch:
            case '1':show_gpu_menu()
            case '2':show_cpu_menu()
            case '3':show_ram_menu()
            case '4':print('4')
            case '5':print('5')
            
    f(ch)
        
            


if __name__=="__main__":
    starting_menu()
    
        