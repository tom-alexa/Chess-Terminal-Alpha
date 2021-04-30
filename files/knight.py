
# Chess in terminal | main ➔ game_loop ➔ game ➔ knight

# imports
from files.piece import Piece


##################
#  knight class  #
##################

# knight
class Knight(Piece):

    # initialize knight
    def __init__(self, color, pos):
        self.short = {1: "", 2: "---- ", 3: "  ---", 4: " ----", 5:""}
        super().__init__(color, pos, "knight")


    # get possible moves
    def get_possible_moves(self, game_data, move_number, board, turn, dimensions, make_move, get_data_at_move, is_check, real=True):

        possible_moves = {"from": self.pos, "to": set()}
        for pos in board:
            if pos != self.pos:
                if ( (pos[0] - 1 == self.pos[0] or pos[0] + 1 == self.pos[0]) and (pos[1] - 2 == self.pos[1] or pos[1] + 2 == self.pos[1]) ) or ( (pos[0] - 2 == self.pos[0] or pos[0] + 2 == self.pos[0]) and (pos[1] - 1 == self.pos[1] or pos[1] + 1 == self.pos[1]) ):
                    valid = self.is_valid(game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos, real)
                    if valid:
                        possible_moves["to"].add(pos)

        return possible_moves


    # is it a valid move
    def is_valid(self, game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos, real):

        if board[pos]:
            if board[pos].color == self.color:
                return False

        if real:
            valid = self.check_if_valid(game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos)
        else:
            valid = False

        return valid
