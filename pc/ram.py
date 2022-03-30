from webscrapping import *
from main import *

def show_ram_menu():
    print(
         "------------------------------------------------------\n"
        +"|                    |RAM MENU|                      |\n"
        +"|----------------------------------------------------|\n"
        +"|1-Check a specific RAM price:                       |\n"
        +"|----------------------------------------------------|\n"
        +"|0-to go back to main menu                           |\n"
        +"|----------------------------------------------------|\n"
        
        )
    ch = input()
    
    def f(ch):
        match ch:
            case '1':search_ram()
            case '0':starting_menu()
            
    f(ch)