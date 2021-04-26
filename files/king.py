
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
        self.short = {1: "", 2: " --- ", 3: "- - -", 4: "-----", 5:""}
        super().__init__(color, pos, "king")


    # get possible moves
    def get_possible_moves(self, board, pieces, dimensions, real=True):

        return True
