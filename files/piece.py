
# Chess in terminal | main ➔ game_loop ➔ game ➔ (king, queen, rook, bishop, knight, pawn) ➔ piece


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

        return valid


    def check_if_not_check(self, board, move_number, turn, game_data, game, move):

        new_game_data, new_move_number, new_turn = game.make_move(game_data, move_number, move, turn)
        poss_moves = game.get_all_possible_moves(new_game_data, new_move_number, new_turn, real=False)

        pieces = game.get_pieces(game.get_data_at_move(new_game_data, new_move_number, new_turn)["board"])[self.color]
        for piece in pieces:
            if piece.description == "king":
                king = piece
                break

        for m in poss_moves:
            if m == king.pos:
                return False

        return True
