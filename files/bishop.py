
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
        self.short = {1: "", 2: "  -  ", 3: " --- ", 4: "-----", 5:""}
        super().__init__(color, pos, "bishop")


    # get possible moves
    def get_possible_moves(self, board, dimensions, move_number, turn, game_data, game, real):

        possible_moves = {"from": self.pos, "to": set()}
        for pos in board:
            if ( pos[0] - pos[1] == self.pos[0] - self.pos[1] ) or ( (dimensions[0] - pos[0]) - pos[1] == (dimensions[0] - self.pos[0]) - self.pos[1] ):
                if pos != self.pos:
                    valid = self.check_if_valid(board, move_number, turn, game_data, game, real, pos)
                    if valid:
                        possible_moves["to"].add(pos)

        return possible_moves
