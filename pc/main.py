from gpu import *
from webscrapping import *
import sys
sys.tracebacklimit=0
def starting_menu():
    print(
        "|----------------------------------------------------------------------|\n"
       +"|             THIS PROGRAM WAS MADE BY SALAH ALHAISMAWI                |\n"
       +"|----------------------------------------------------------------------|\n"
       +"|1-To view Graphic cards and thier benchmarks.                          |\n" 
       +"|2-To view CPU's and thier benchmarks.                                  |\n"
       +"|3-To view RAM Models.                                                  |\n"
       +"|4-To Choose a recommended psu depending on your need.                 |\n"
       +"|5-To pick a Stylish Case for your needs.                               |\n"
       +"|----------------------------------------------------------------------|\n"    
    )
    
    ch = input()
    
    def f(ch):
        match ch:
            case '1':show_gpu_menu()
            case '2':print('2')
            case '3':print('3')
            case '4':print('4')
            case '5':print('5')
            
    f(ch)
        
            


if __name__=="__main__":
    starting_menu()
    
        