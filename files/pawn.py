
# Chess in terminal | main ➔ game_loop ➔ game ➔ pawn

# imports
from files.piece import Piece


#################
#  pawn object  #
#################

# pawn
class Pawn(Piece):

    # initial pawn
    def __init__(self, color, pos):
        super().__init__(color, pos, "pawn")
