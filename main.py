
# Chess in terminal | main
# Author: Tom Alexa

# You can play game chess in terminal

# imports
from files.game_loop import game_loop
from files.terminal import main_terminal
from files.user_input import user_input


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

    introduction()
    op_sys = operating_system()
    game_loop(op_sys)
    ending()


# main
if __name__ == "__main__":
    main()
