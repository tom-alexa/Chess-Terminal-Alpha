
# Chess in terminal | main
# Author: Tom Alexa

# You can play game chess in terminal

# imports
from files.game_loop import game_loop


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
    pass


# ending
def ending():
    pass


##########
#  main  #
##########

# main function
def main():

    introduction()
    game_loop()
    ending()


# main
if __name__ == "__main__":
    main()
