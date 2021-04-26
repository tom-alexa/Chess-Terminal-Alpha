
# Chess in terminal | main ➔ game_loop ➔ game ➔ (king, queen, rook, bishop, knight, pawn) ➔ piece


##################
#  piece object  #
##################

# piece
class Piece():

    # initial piece
    def __init__(self, color, pos, description):

        # parameters
        self.color = color
        self.pos = pos
        self.description = description

    def check_if_valid(self, board):

        return True
