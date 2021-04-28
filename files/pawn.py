
# Chess in terminal | main ➔ game_loop ➔ game ➔ pawn

# imports
from files.piece import Piece


#################
#  pawn object  #
#################

# pawn
class Pawn(Piece):

    # initial pawn
    def __init__(self, color, pos):
        super().__init__(color, pos, "pawn")

        self.short = {1: "", 2: "", 3: "  -  ", 4: " --- ", 5:""}
        self.first_move = True


    # get possible moves
    def get_possible_moves(self, game_data, move_number, board, turn, dimensions, make_move, get_data_at_move, is_check, real=True):

        step = 1 if self.color == "white" else -1
        possible_moves = {"from": self.pos, "to": set()}
        for pos in board:
            if pos != self.pos:
                if (pos[0] == self.pos[0] + step) and ( (pos[1] == self.pos[1] - 1) or (pos[1] == self.pos[1]) or (pos[1] == self.pos[1] + 1) ) or ( ( pos[0] == self.pos[0] + (2 * step) ) and (pos[1] == self.pos[1]) and self.first_move ):
                    valid = self.is_valid(game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos, real)

                    if valid:
                        possible_moves["to"].add(pos)

        return possible_moves


    # is it a valid move
    def is_valid(self, game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos, real):

        if pos[1] == self.pos[1]:
            valid = self.check_row_column(board, pos, pawn=True)
        else:
            valid = self.check_diagonal(board, pos, pawn=True)

        if valid and real:
            valid = self.check_if_valid(game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos)

        return valid
