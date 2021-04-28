
# Chess in terminal | main ➔ game_loop ➔ game

# imports
from files.king import King
from files.queen import Queen
from files.rook import Rook
from files.bishop import Bishop
from files.knight import Knight
from files.pawn import Pawn
from files.terminal import terminal_board
from files.user_input import user_input
import copy


#################
#  game object  #
#################

# game
class Game():

    # initial game
    def __init__(self, number_of_players, difficulty, names, player_color):

        # parameters
        self.number_of_players = number_of_players
        self.difficulty = difficulty
        self.names = names
        self.player_color = player_color

        # variables
        self.dimensions = (8, 8)            # (rows, columns)
        self.move_number = 0
        start_board = self.create_board()
        self.game_data = {self.move_number: {"board": start_board } }
        self.turn = -1

        # colors
        self.colors = self.board_colors()


    # create board
    def create_board(self):

        board = {}
        # create board | { (row, column): None }
        for row in range(1, self.dimensions[0]+1):
            for column in range(1, self.dimensions[1]+1):
                board[(row, column)] = None

        board = self.create_pieces(board)

        return board


    # create pieces
    def create_pieces(self, board):
        
        for color in ["white", "black"]:

            # pieces
            row = 1 if color == "white" else 8

            # king
            column = 5
            king = King(color, (row, column))
            board[(row, column)] = king

            # queen
            column = 4
            queen = Queen(color, (row, column))
            board[(row, column)] = queen

            # rook
            for column in [1, 8]:
                rook = Rook(color, (row, column))
                board[(row, column)] = rook


            # knight
            for column in [2, 7]:
                knight = Knight(color, (row, column))
                board[(row, column)] = knight

            # bishop
            for column in [3, 6]:
                bishop = Bishop(color, (row, column))
                board[(row, column)] = bishop

            # pawn
            row = 2 if color == "white" else 7
            for column in range(1, self.dimensions[0]+1):
                pawn = Pawn(color, (row, column))
                board[(row, column)] = pawn

        return board


    def board_colors(self):

        colors = {}
        colors["pl_1"] = "red"
        colors["pl_2"] = "black"
        colors["bg_1"] = "blue"
        colors["bg_2"] = "cyan"

        return colors


    ##########
    #  play  #
    ##########

    # play (this is where actual game is happening)
    def play(self):

        # running while game is launched
        playing = True
        while playing:

            terminal_board(self.get_data_at_move(self.game_data, self.move_number, self.turn)["board"], self.dimensions, self.colors)

            # move
            move = self.get_move()
            self.game_data, self.move_number, self.turn = self.make_move(self.game_data, self.move_number, move, self.turn)


            # check if game is finished
            mate = self.checkmate(self.game_data, self.move_number, self.get_data_at_move(self.game_data, self.move_number, self.turn)["board"], self.turn)
            if mate:
                terminal_board(self.get_data_at_move(self.game_data, self.move_number, self.turn)["board"], self.dimensions, self.colors)
                playing = False


    ############
    #  phases  #
    ############

    # get move
    def get_move(self):

        # choose who will do the move
        if self.number_of_players == 2:
            move = self.player_move()
        elif self.number_of_players == 1:
            if ( (self.turn * -1) > 0 and self.player_color == "white") or ( (self.turn * -1) < 0 and self.player_color == "black"):
                move = self.player_move()
            else:
                move = self.computer_move()
        else:
            move = self.computer_move()

        return move


    # make move
    def make_move(self, game_data, move_number, move, turn):

        # get current board
        board = copy.deepcopy(self.get_data_at_move(game_data, move_number, turn)["board"])

        # change turn
        turn *= -1

        # update move number and turn
        if turn > 0:
            move_number += 1

        # position
        from_pos = move["pos"]["from"]
        to_pos = move["pos"]["to"]

        # piece
        active_piece = board[from_pos]

        # make move
        board[from_pos] = None
        board[to_pos] = active_piece
        active_piece.pos = to_pos

        # special
        move["castling"] = False
        move["en passant"] = False

        if active_piece.description == "pawn":
            active_piece.first_move = False

        if move["castling"]:
            pass

        if move["en passant"]:
            pass

        # update data
        if turn > 0:
            game_data[move_number] = {turn: {"board": board} }
        else:
            game_data[move_number][turn] = {"board": board}


        return game_data, move_number, turn


    # get possible moves
    def get_all_possible_moves(self, game_data, move_number, turn, real=True):

        # moves that can only be played by player on the turn
        color = "white" if turn < 0 else "black"

        possible_moves = {}
        board = self.get_data_at_move(game_data, move_number, turn)["board"]
        pieces = self.get_pieces(board)[color]
        for piece in pieces:
            moves = piece.get_possible_moves(game_data, move_number, board, turn, self.dimensions, self.make_move, self.get_data_at_move, self.is_check)
            possible_moves[moves["from"]] = moves["to"]

        return possible_moves


    ##########################
    #  move ➔ subfunctions  #
    ##########################

    # player move
    def player_move(self):

        while True:
            move = {}
            move_input = user_input("move")
            move["pos"] = {}
            move["pos"]["from"] = self.get_pos(move_input[:2])
            move["pos"]["to"] = self.get_pos(move_input[2:])

            valid = False
            poss_moves = self.get_all_possible_moves(self.game_data, self.move_number, self.turn)
            for poss_move_from in poss_moves:
                if valid:
                    break
                if move["pos"]["from"] == poss_move_from:
                    for poss_move_to in poss_moves[poss_move_from]:
                        if move["pos"]["to"] == poss_move_to:
                            valid = True
                            break

            if valid:
                break
        
        return move


    # computer move
    def computer_move(self):

        move = self.player_move()
        return move


    ###################
    #  get something  #
    ###################

    # function return all pieces which are in the given color
    def get_pieces(self, board):

        pieces = {"white": set(), "black": set()}
        for pos in board:
            if board[pos]:
                piece = board[pos]
                clr = piece.color
                pieces[clr].add(piece)

        return pieces


    # get game data at the exact moment board
    def get_data_at_move(self, game_data, move_number, turn):

        if move_number < 1:
            data = game_data[move_number]
        else:
            data = game_data[move_number][turn]

        return data


    # function return position in format (row, column) form format (letter(column), row(string))
    def get_pos(self, string):

        column = int( ord(string[0].upper() ) ) - 64
        row = int(string[1])

        return (row, column)


    def get_move_before(self, move_number, turn):
        
        if turn > 1:
            move_number -= 1
        turn *= -1

        return move_number, turn


    def get_castling(self):
        pass

    def enpassant(self):
        pass


    ###########
    #  check  #
    ###########

    # detect check
    def is_check(self, game_data, move_number, board, turn, attack=True):

        clr = "white" if turn > 0 else "black"
        opp_clr = "white" if turn < 0 else "black"


        pieces = self.get_pieces(board)

        king_color = opp_clr if attack else clr
        for piece in pieces[king_color]:
            if piece.description == "king":
                king_pos = piece.pos
                break

        pieces_clr = clr if attack else opp_clr
        for piece in pieces[pieces_clr]:
            moves = piece.get_possible_moves(game_data, move_number, board, turn, self.dimensions, self.make_move, self.get_data_at_move, self.is_check, real=False)
            for move in moves["to"]:
                if move == king_pos:
                    return True

        return False


    def checkmate(self, game_data, move_number, board, turn):


        check = self.is_check(game_data, move_number, board, turn)

        return check
