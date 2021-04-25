
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
        super().__init__(color, pos, "knight", f"{color[0]}N")
