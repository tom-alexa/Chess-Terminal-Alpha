
# Chess in terminal | main
# Author: Tom Alexa

# You can play game chess in terminal

# imports
from files.game_loop import game_loop
from files.terminal import Terminal


# structure | main ➔ game_loop ➔ game ➔  king  ➔ piece
#                                       🢆 queen 🢅
#                                       🢆 rook  🢅
#                                       🢆 bishop🢅
#                                       🢆 knight🢅
#                                       🢆 pawn  🢅


############
#  phases  #
############

# introduction
def introduction():
    main_terminal("introduction", operating_system=None)


# get operating system
def operating_system():
    while True:
        op_sys = user_input("operating system")
        if op_sys != "unknown" and op_sys != "no command":
            return op_sys


# ending
def ending():
    main_terminal("ending")


##########
#  main  #
##########

# main function
def main():

    terminal = Terminal()
    # introduction()
    # op_sys = operating_system()
    game_loop(terminal)
    ending()


# main
if __name__ == "__main__":
    main()
