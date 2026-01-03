from src.utils import *
from src.auth import login
from src.admin import admin_menu
from src.game import new_game
from src.stats import show_history, show_stats, show_help

def ahorcado():
    while True:
        clear_screen()
        print(get_msg('MAIN_MENU').center(50, "="))
        print(get_msg('OPT_ADMIN'))
        print(get_msg('OPT_PLAYER'))
        print(get_msg('OPT_EXIT'))
        
        print("\n" + get_msg('PROMPT'), end="")
        op = my_strip(input()).upper()
        
        if op == 'A':
            if login():
                admin_menu()
            else:
                pause()
        elif op == 'J' or op == 'P': # J for Jugador, P for Player (if English)
            # Submenu for Player
            while True:
                clear_screen()
                print(get_msg('PLAYER_MENU').center(50, "="))
                print(f"(1) {get_msg('OPT_NEW_GAME')}")
                print(f"(2) {get_msg('OPT_HISTORY')}")
                print(f"(3) {get_msg('OPT_STATS')}")
                print(f"(4) {get_msg('OPT_HELP')}")
                print(f"(R) {get_msg('OPT_RETURN')}")
                
                print("\n" + get_msg('PROMPT'), end="")
                pop = my_strip(input()).upper()
                
                if pop == '1':
                    new_game()
                elif pop == '2':
                    show_history()
                elif pop == '3':
                    show_stats()
                elif pop == '4':
                    show_help()
                elif pop == 'R':
                    break
                else:
                    print(get_msg('INVALID_OPT'))
                    pause()
                    
        elif op == 'S':
            break
        else:
            print(get_msg('INVALID_OPT'))
            pause()

if __name__ == "__main__":
    ahorcado()
