
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
        super().__init__(color, pos, "king")

        self.short = {1: "", 2: " --- ", 3: "- - -", 4: "-----", 5:""}
        self.castling = {"big": True, "small": True}


    # get possible moves
    def get_possible_moves(self, board, dimensions, move_number, turn, game_data, game, real):

        possible_moves = {"from": self.pos, "to": set()}
        for pos in board:
            if (pos[0] == self.pos[0] - 1) or (pos[0] == self.pos[0]) or (pos[0] == self.pos[0] + 1):
                if (pos[1] == self.pos[1] - 1) or (pos[1] == self.pos[1]) or (pos[1] == self.pos[1] + 1):
                    if pos != self.pos:
                        valid = self.check_if_valid(board, move_number, turn, game_data, game, real, pos)
                        if valid:
                            possible_moves["to"].add(pos)

        return possible_moves
