
# Chess in terminal | main ➔ game_loop ➔ game ➔ (king, queen, rook, bishop, knight, pawn) ➔ piece

# imports
import copy


##################
#  piece object  #
##################

# piece
class Piece():

    # initial piece
    def __init__(self, color, pos, description):

        # parameters
        self.color = color
        self.pos = pos
        self.description = description


    # function tells you if king is in check position, therefore it is forbidden
    def check_if_valid(self, game_data, move_number, board, turn, make_move, get_data_at_move, is_check, move):

        copy_data = copy.deepcopy(game_data)
        mod_move = {"pos": {"from": self.pos, "to": move} }
        mod_board = get_data_at_move(copy_data, move_number, turn)["board"]
        data, move_number, turn = make_move(copy_data, move_number, mod_move, turn)

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
    def check_diagonal(self, board, pos, pawn=False):

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
                return False

        return True
