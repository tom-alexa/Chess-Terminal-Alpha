
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
    def get_possible_moves(self, game_data, move_number, board, turn, dimensions, make_move, get_data_at_move, is_check, real=True):

        possible_moves = {"from": self.pos, "to": set()}
        for pos in board:
            if pos != self.pos:
                if (pos[0] == self.pos[0] - 1) or (pos[0] == self.pos[0]) or (pos[0] == self.pos[0] + 1):
                    if (pos[1] == self.pos[1] - 1) or (pos[1] == self.pos[1]) or (pos[1] == self.pos[1] + 1):
                        valid = self.is_valid(game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos, real)
                        if valid:
                            possible_moves["to"].add(pos)

        return possible_moves


    # is it a valid move
    def is_valid(self, game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos, real):

        if pos[0] == self.pos[0] or pos[1] == self.pos[1]:
            valid = self.check_row_column(board, pos)
        else:
            valid = self.check_diagonal(board, pos)

        if valid and real:
            valid = self.check_if_valid(game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos)

        return valid
