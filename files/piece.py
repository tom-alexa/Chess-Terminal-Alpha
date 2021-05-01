
# Chess in terminal | main ➔ game_loop ➔ game ➔ (king, queen, rook, bishop, knight, pawn) ➔ piece

# imports
import copy


#################
#  piece class  #
#################

# piece
class Piece():

    # initialize piece
    def __init__(self, player_id, description, pos):

        # parameters
        self.player_id = player_id
        self.description = description
        self.pos = pos


    ###################
    #  possible move  #
    ###################

    # function tells you if king is in check position, therefore it is forbidden
    def is_move_possible(self, game_data, move_index, pos, check_matter, *args, **kwargs):

        current_data = kwargs["get_data_at_move"](game_data, move_index)

        if self.is_in_potencial_moves(current_data, pos):
            if self.is_valid(current_data, pos):
                if check_matter:

                    move = {"pos": {"from": self.pos, "to": pos} }
                    move["castling"] = True if kwargs["is_castling"](current_data["board"], move) else False
                    move["en_passant"] = kwargs["is_en_passant"](current_data, move)

                    new_data = copy.deepcopy(game_data)
                    kwargs["make_move"](new_data, move_index, move)
                    if not kwargs["is_in_check"](new_data, move_index, self.player_id):
                        return True
                else:
                    return True


    #####################################
    #  possible move ➔ check position  #
    #####################################

    # check row
    def check_row_column(self, board, pos):

        if pos[0] == self.pos[0]:
            same_index = 0
            change_index = 1
        else:
            same_index = 1
            change_index = 0

        if pos[change_index] < self.pos[change_index]:
            multiply = 1
        else:
            multiply = -1

        diff = abs(pos[change_index] - self.pos[change_index])
        for i in range(diff):
            if same_index == 0:
                check_pos = (pos[0], pos[1] + (i * multiply))
            else:
                check_pos = (pos[0] + (i * multiply), pos[1])

            if board[check_pos]:
                if board[check_pos].color == self.color:
                    return False
                else:
                    if (check_pos != pos) or self.description == "pawn":
                        return False

        return True


    # check column
    def check_diagonal(self, board, pos, last_move=None):

        if pos[0] - pos[1] == self.pos[0] - self.pos[1]:
            change_meta = 1
        else:
            change_meta = -1

        if pos[0] > self.pos[0]:
            first = 1
            second = change_meta
        else:
            first = -1
            second = first * change_meta

        diff = abs(pos[0] - self.pos[0])
        for i in range(diff):
            check_pos = (pos[0] - (i * first), pos[1] - (i * second))

            if board[check_pos]:
                if board[check_pos].color == self.color:
                    return False
                else:
                    if check_pos != pos:
                        return False

            elif self.description == "pawn":                # en passant
                if last_move:
                    if (board[last_move["pos"]["to"]].description == "pawn") and  (last_move["to"][0] == self.pos[0]) and (last_move["pos"]["to"][1] == pos[1]):
                        return True
                    else:
                        return False
                else:
                    return False
        return True
