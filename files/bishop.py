
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
        super().__init__(color, pos, "bishop", f"{color[0]}B")
