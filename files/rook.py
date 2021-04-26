
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
        self.short = {1: "", 2: "- - -", 3: " --- ", 4: "-----", 5: ""}
        super().__init__(color, pos, "rook")

    # get possible moves
    def get_possible_moves(self, board, get_dimensions):
        pass
