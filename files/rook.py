
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
    def get_possible_moves(self, board, dimensions):

        possible_moves = {"from": self.pos, "to": set()}
        for pos in board:
            if pos != self.pos:
                if (pos[0] == self.pos[0]) or (pos[1] == self.pos[1]):
                    valid = self.is_valid(board, pos)
                    if valid:
                        possible_moves["to"].add(pos)

        return possible_moves


    # is it a valid move
    def is_valid(self, board, pos):

        valid = self.check_row_column(board, pos)
        return valid
