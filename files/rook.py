
# Chess in terminal | main ➔ game_loop ➔ game ➔ rook

# imports
from files.piece import Piece


#################
#  rook object  #
#################

# rook
class Rook(Piece):

    # initial rook
    def __init__(self, color, pos):
        super().__init__(color, pos, "rook", f"{color[0]}R")
