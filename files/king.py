
# Chess in terminal | main ➔ game_loop ➔ game ➔ king

# imports
from files.piece import Piece


################
#  king class  #
################

# king
class King(Piece):

    # initialize king
    def __init__(self, player_id, pos):
        super().__init__(player_id, "king", pos)

        self.short = {1: "", 2: " --- ", 3: "- - -", 4: "-----", 5:""}


    # get possible moves
    def is_move_valid(self, game_data, move_number, board, turn, dimensions, make_move, get_data_at_move, is_check, pos, real=True):

        valid = False
        if pos != self.pos:
            if (pos[0] == self.pos[0] - 1) or (pos[0] == self.pos[0]) or (pos[0] == self.pos[0] + 1):
                if (pos[1] == self.pos[1] - 1) or (pos[1] == self.pos[1]) or (pos[1] == self.pos[1] + 1):
                    valid = self.is_valid(game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos, real)

        return valid


    # is it a valid move
    def is_valid(self, game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos, real):

        if pos[0] == self.pos[0] or pos[1] == self.pos[1]:
            valid = self.check_row_column(board, pos)
        else:
            valid = self.check_diagonal(board, pos)

        if valid and real:
            valid = self.check_if_valid(game_data, move_number, turn, make_move, get_data_at_move, is_check, pos)

        return valid
