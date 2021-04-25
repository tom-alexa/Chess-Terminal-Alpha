
# Chess in terminal | main ➔ game_loop ➔ game ➔ king

# imports
from files.piece import Piece


#################
#  king object  #
#################

# king
class King(Piece):

    # initial king
    def __init__(self, color, pos):
        super().__init__(color, pos, "king")
