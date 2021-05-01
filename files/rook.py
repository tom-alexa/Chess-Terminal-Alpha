
# Chess in terminal | main ➔ game_loop ➔ game ➔ rook

# imports
from files.piece import Piece


################
#  rook class  #
################

# rook
class Rook(Piece):

    # initialize rook
    def __init__(self, player_id, pos):
        self.short = {1: "", 2: "- - -", 3: " --- ", 4: "-----", 5: ""}
        super().__init__(player_id, "rook", pos)


    # get possible moves
    def is_in_potencial_moves(self, current_data, pos):

        if pos != self.pos:
            if (pos[0] == self.pos[0] - 1) or (pos[0] == self.pos[0]) or (pos[0] == self.pos[0] + 1):               # one square far
                if (pos[1] == self.pos[1] - 1) or (pos[1] == self.pos[1]) or (pos[1] == self.pos[1] + 1):
                    return True



    # is it a valid move
    def is_valid(self, current_data, pos):

        if pos[0] == self.pos[0] or pos[1] == self.pos[1]:
            return self.check_row_column(current_data["board"], pos)
        else:
            return self.check_diagonal(current_data["board"], pos)









    # # get possible moves
    # def get_possible_moves(self, game_data, move_number, board, turn, dimensions, make_move, get_data_at_move, is_check, real=True):

    #     possible_moves = {"from": self.pos, "to": set()}
    #     for pos in board:
    #         if pos != self.pos:
    #             if (pos[0] == self.pos[0]) or (pos[1] == self.pos[1]):
    #                 valid = self.is_valid(game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos, real)
    #                 if valid:
    #                     possible_moves["to"].add(pos)

    #     return possible_moves


    # # is it a valid move
    # def is_valid(self, game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos, real):

    #     valid = self.check_row_column(board, pos)

    #     if valid and real:
    #         valid = self.check_if_valid(game_data, move_number, board, turn, make_move, get_data_at_move, is_check, pos)

    #     return valid
