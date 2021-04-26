
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
        self.short = {1: "", 2: "", 3: "  -  ", 4: " --- ", 5:""}
        super().__init__(color, pos, "pawn")


    # get possible moves
    def get_possible_moves(self, board, get_dimensions):

        pass