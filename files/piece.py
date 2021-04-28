
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


    def check_if_valid(self, board, move_number, turn, game_data, game, real, move):

        valid = True
        if real:
            pass
            # valid = self.check_if_not_check(board, move_number, turn, game_data, game, move)
        new_game_data, new_move_number, new_turn = game.make_move(copy.deepcopy(game_data), move_number, move, turn)
        poss_moves = game.get_all_possible_moves(new_game_data, new_move_number, new_turn, real=False)

        pieces = game.get_pieces(game.get_data_at_move(new_game_data, new_move_number, new_turn)["board"])[self.color]
        for piece in pieces:
            if piece.description == "king":
                king = piece
                break

        for m in poss_moves:
            if m == king.pos:
                return False


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
