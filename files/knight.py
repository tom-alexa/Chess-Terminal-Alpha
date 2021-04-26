
# Chess in terminal | main ➔ game_loop ➔ game ➔ knight

# imports
from files.piece import Piece


###################
#  knight object  #
###################

# knight
class Knight(Piece):

    # initial knight
    def __init__(self, color, pos):
        self.short = {1: "", 2: "---- ", 3: "  ---", 4: " ----", 5:""}
        super().__init__(color, pos, "knight")

    # get possible moves
    def get_possible_moves(self, board, get_dimensions):
        pass
