
# Chess in terminal | main ➔ game_loop ➔ game ➔ (king, queen, rook, bishop, knight, pawn) ➔ piece


##################
#  piece object  #
##################

# piece
class Piece():

    # initial piece
    def __init__(self, color, pos, description, short):

        # parameters
        self.color = color
        self.pos = pos
        self.description = description
        self.short = short

