from webscrapping import *
from main import *

def show_cpu_menu():
      print(
        "------------------------------------------------------\n"
       +"|                |CPU MENU|                          |\n"
       +"|----------------------------------------------------|\n"
       +"|1-Check a specific CPU price                        |\n"
       +"|----------------------------------------------------|\n"
       +"|0-Go back to main menu                              |\n"
       +"|----------------------------------------------------|\n"
    )
      ch=input()
      def f(ch):
        match ch:
            case '1': search_cpu()  
            case '0': starting_menu()    
    
      f(ch)