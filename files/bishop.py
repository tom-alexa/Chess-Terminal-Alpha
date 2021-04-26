
# Chess in terminal | main ➔ game_loop ➔ game ➔ bishop

# imports
from files.piece import Piece


###################
#  bishop object  #
###################

# bishop
class Bishop(Piece):

    # initial bishop
    def __init__(self, color, pos):
        self.short = {1: "", 2: "  -  ", 3: " --- ", 4: "-----", 5:""}
        super().__init__(color, pos, "bishop")


    # get possible moves
    def get_possible_moves(self, board, get_dimensions):
        pass
