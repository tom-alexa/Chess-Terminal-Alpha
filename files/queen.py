
# Chess in terminal | main ➔ game_loop ➔ game ➔ queen

# imports
from files.piece import Piece


##################
#  queen object  #
##################

# queen
class Queen(Piece):

    # initial queen
    def __init__(self, color, pos):
        self.short = {1: "", 2: "- - -", 3: "-----", 4: "-----", 5:""}
        super().__init__(color, pos, "queen")

    # get possible moves
    def get_possible_moves(self, board, get_dimensions):
        pass
