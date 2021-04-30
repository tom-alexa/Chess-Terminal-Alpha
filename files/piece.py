
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


    # function tells you if king is in check position, therefore it is forbidden
    def check_if_valid(self, game_data, move_number, turn, make_move, get_data_at_move, is_check, move):

        copy_data = copy.deepcopy(game_data)
        mod_move = {"pos": {"from": self.pos, "to": move} }
        mod_board = get_data_at_move(copy_data, move_number, turn)["board"]
        data, move_number, turn = make_move(copy_data, move_number, turn, mod_move)

        valid = not (is_check(data, move_number, get_data_at_move(data, move_number, turn )["board"], turn, attack=False) )

        return valid


    ####################
    #  check position  #
    ####################

    # check row
    def check_row_column(self, board, pos, pawn=False):

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
                    if (check_pos != pos) or pawn:
                        return False

        return True


    # check column
    def check_diagonal(self, board, pos, pawn=False, last_move=None):

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
            elif pawn:
                mod = 1 if self.color == "white" else -1
                if last_move:
                    if (board[last_move["to"]].description == "pawn") and ( (last_move["to"][0] + (1 * mod), last_move["to"][1] ) == pos):
                        return True
                    else:
                        return False
                else:
                    return False

        return True
