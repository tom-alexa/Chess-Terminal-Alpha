
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
def introduction(terminal):
    terminal.introduction()


# ending
def ending(terminal):
    terminal.ending()


##########
#  main  #
##########

# main function
def main():

    terminal = Terminal()
    introduction(terminal)
    game_loop(terminal)
    ending(terminal)


# main
if __name__ == "__main__":
    main()
