
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
        super().__init__(color, pos, "queen")
