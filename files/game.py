
# Chess in terminal | main ➔ game_loop ➔ game

# imports
from files.king import King
from files.queen import Queen
from files.rook import Rook
from files.bishop import Bishop
from files.knight import Knight
from files.pawn import Pawn
import copy


#################
#  game object  #
#################

# game
class Game():

    ################
    #  initialize  #
    ################

    # initialize game
    def __init__(self, terminal, number_of_players, human_players_id, difficulty, names, dimensions=(8, 8)):

        # parameters
        self.terminal = terminal                        # terminal where everything is printed
        self.user_input = self.terminal.user_input      # where we get all user inputs
        self.number_of_players = number_of_players      # including either bots and human players
        self.human_players_id = human_players_id        # set contains ids of human players
        self.difficulty = difficulty                    # how difficult it is to beat the bot
        self.names = names                              # players names (bots has "BOT" before name)
        self.dimensions = dimensions                    # (rows, columns)

        # game data
        move_number = 0                                 # each player plays once in every turn until game is finished
        turn = self.number_of_players - 1               # turn and move number are data about last move, so it is NOT saying whose turn it is NOW
        self.move_index = {"move_number": move_number, "turn": turn}

        # main unit (stores data about every move, if you look inside you can see data about moves you want)
        self.game_data = {move_number: {"board": self.create_board(self.dimensions, self.number_of_players), "castling": self.create_castling(self.number_of_players), "check": self.create_check(self.number_of_players), "checkmate": self.create_check(self.number_of_players), "stalemate": self.create_check(self.number_of_players), "last_pawn_move": move_number } }

        # colors
        self.colors = self.board_colors()               # data about game color, how terminal will visualize the game


    #########################
    #  initialize ➔ board  #
    #########################

    # create board with pieces on it
    def create_board(self, dimensions, number_of_players):

        board = {}
        # create board | { (row, column): None }
        for row in range(1, self.dimensions[0]+1):
            for column in range(1, self.dimensions[1]+1):
                board[(row, column)] = None

        self.create_pieces(board, number_of_players)
        return board


    # create pieces on the board
    def create_pieces(self, board, number_of_players):

        for player_id in range(number_of_players):
            if number_of_players == 2:

                # pieces
                row = 1 if player_id == 0 else 8

                # king
                column = 5
                king = King(player_id, (row, column))
                board[(row, column)] = king

                # queen
                column = 4
                queen = Queen(player_id, (row, column))
                board[(row, column)] = queen

                # # rook
                # for column in [1, 8]:
                #     rook = Rook(color, (row, column))
                #     board[(row, column)] = rook


                # # knight
                # for column in [2, 7]:
                #     knight = Knight(color, (row, column))
                #     board[(row, column)] = knight

                # # bishop
                # for column in [3, 6]:
                #     bishop = Bishop(color, (row, column))
                #     board[(row, column)] = bishop

                # # pawn
                # row = 2 if player_id == 0 else 7
                # for column in range(1, self.dimensions[0]+1):
                #     pawn = Pawn(color, (row, column))
                #     board[(row, column)] = pawn


    ####################################
    #  initialize ➔ castling / check  #
    ####################################

    # create castling rights
    def create_castling(self, number_of_players, yes_or_no=True):

        castling = {}
        for player_id in range(number_of_players):
            castling[player_id] = {}
            for side in range(2):   # left: 0, right: 1
                castling[player_id][side] = yes_or_no

        return castling


    # create check
    def create_check(self, number_of_players, yes_or_no=False):

        check = {}
        for player_id in range(number_of_players):
            check[player_id] = yes_or_no

        return check


    # board colors
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

        playing = True
        while playing:                                                              # running while game is launched

            self.manage_move(self.game_data, self.move_index, self.human_players_id)    # make move
            if self.is_game_finished(self.game_data, self.move_index):                  # check if game is finished
                playing = False


    ####################
    #  play ➔ phases  #
    ####################

    # manage move
    def manage_move(self, game_data, move_index, human_players_id):

        move = self.get_move(game_data, move_index, human_players_id)   # get move
        self.make_move(game_data, move_index, move)                     # make move


    # return if game is finished
    def is_game_finished(self, game_data, move_index):
        
        # if checkmate or stalemate
        if game_data[move_index["move_number"]][move_index["turn"]]["checkmate"] or game_data[move_index["move_number"]][move_index["turn"]]["stalemate"]:
            return True
        else:
            return False



    #########################
    #  play ➔ manage_move  #
    #########################

    # calls either computer move or player move, depents which turn it is
    def get_move(self, game_data, move_index, human_players_id):

        # which turn it is
        human = False
        for player_id in human_players_id:
            if player_id == move_index["turn"]:
                human = True
                break

        # get move
        move = self.player_move(game_data, move_index) if human else self.computer_move(game_data, move_index)
        return move



    ####################################
    #  play ➔ manage_move ➔ get_move  #
    ####################################

    # player move
    def player_move(self, game_data, move_index):

        # get all possible moves
        possible_moves = self.get_all_possible_moves(game_data, move_index)

        # get user input
        while True:
            move_input = self.user_input.main("move")
            move = { "pos": {"from": self.get_pos(move_input[:2]), "to": self.get_pos(move_input[2:]) } }

            poss_moves_to = possible_moves[move["pos"]["from"]]
            for poss_move in poss_moves_to:
                if poss_move == move["pos"]["to"]:
                    return move
            print("not in possible moves")


    # computer move
    def computer_move(self):

        move = self.player_move()
        return move


    #########################
    #  play ➔ manage_move  #
    #########################

    # make move
    def make_move(self, game_data, move_index, move):

        # current data
        current_data = copy.deepcopy(self.get_data_at_move(game_data, move_index))

        # change turn and (if..) move number
        self.change_move_index(move_index)

        # make actual move
        self.make_actual_move(current_data, move_index, move)

        if move["castling"]:
            self.castling(current_data["board"], move_index["turn"], move)
        elif move["en_passant"]:
            self.en_passant(current_data["board"])

        self.update_move(current_data, move_index, move)
        self.add_data(game_data, move_index, current_data)


    ###############################################
    #  play ➔ phases ➔ manage_move ➔ make_move  #
    ###############################################

    # increase current move index
    def change_move_index(self, move_index, up=True):

        # new turn and (if..) move number
        if up:
            move_index["turn"] += 1
            if move_index["turn"] >= self.number_of_players:
                move_index["turn"] = 0
                move_index["move_number"] += 1
        else:
            move_index["turn"] -= 1
            if move_index["turn"] < 0:
                move_index["turn"] = self.number_of_players - 1
                move_index["move_number"] -= 1


    # make actual move
    def make_actual_move(self, board, move):

        # move piece from old position to new position and change piece attribute pos
        active_piece = board[move["pos"]["from"]]
        active_piece.pos = move["pos"]["to"]
        board[move["pos"]["from"]] = None
        board[move["pos"]["to"]] = active_piece


    # update data about move
    def update_move(self, current_data, move_index, move):

        # last move
        current_data["last_move"] = copy.deepcopy(move)

        # last pawn move
        if active_piece.description == "pawn":
            active_piece.first_move = False
            current_data["last_pawn_move"] = move_index["move_number"]

        # castling rights
        elif active_piece.description == "king":
            current_data["castling"][move_index["turn"]] = {0: False, 1: False}

        elif active_piece == "rook":
            if (self.dimensions[1] + 1 - active_piece.pos[1]) >= (self.dimensions[1]//2):
                current_data["castling"][move_index["turn"]][0] = False
            else:
                current_data["castling"][move_index["turn"]][1] = False


        # check / checkmate / stalemate
        for player_id in check_ids:                    # for every player
            if self.is_check(game_data, move_index, player_id):             # check
                current_data["check"][player_id] = True
                current_data["stalemate"][player_id] = False


                if self.are_there_moves(game_data, move_index, player_id):  # if check, are there possible moves, if not checkmate
                    current_data["checkmate"][player_id] = True
                else:
                    current_data["checkmate"][player_id] = False
            else:                                                           # if not check, are there possible moves, if not stalemate
                current_data["check"][player_id] = False
                current_data["checkmate"][player_id] = False

                if self.are_there_moves(game_data, move_index, player_id):
                    current_data["stalemate"][player_id] = True
                else:
                    current_data["stalemate"][player_id] = False


    # castling
    def castling(self, board, player_id, move):

        # find king position
        king_pos = self.find_pos_of_piece("king", board, player_id)[0]

        if (self.dimensions[1] + 1 - move["pos"]["to"]) >= (self.dimensions[1]//2):
            self.make_actual_move(board, {"pos": {"from": (king_pos[0], 1), "to": (king_pos[0], king_pos[1] + 1) } } )                      # left
        else:
            self.make_actual_move(board, {"pos": {"from": (king_pos[0], self.dimensions[1]), "to": (king_pos[0], king_pos[1] - 1) } } )     # right


    # en passant
    def en_passant(self, board, move):

        # delete pawn from the board
        board[(move["pos"]["from"][0], move["pos"]["to"][1])] = None



    # add data in the game data
    def add_data(self, game_data, move_index, data):

        # add current data in the game data
        if move_index["turn"] == 0:
            game_data[move_index["move_number"]] = {move_index["turn"]: data}
        else:
            game_data[move_index["move_number"]][move_index["turn"]] = data


    ###################
    #  get something  #
    ###################

    # find king/queen/rook/bishop/knight/pawn position
    def find_pos_of_piece(self, piece_desc, board, player_id):

        # check every position
        positions = set()
        for pos in board:
            if board[pos].description == piece_desc and board[pos].player_id == player_id:
                positions.add(pos)
        
        return positions


    # function return all pieces which belongs to the given player id
    def get_pieces(self, board, player_id):

        pieces = set()
        for pos in board:
            if board[pos]:
                if board[pos].player_id == player_id:
                    pieces.add(board[pos])

        return pieces


    # get game data at the exact moment board
    def get_data_at_move(self, game_data, move_index):

        if move_index["move_number"] < 1:
            data = game_data[move_index["move_number"]]
        else:
            data = game_data[move_index["move_number"]][move_index["turn"]]

        return data


    # function return position in format (row, column) form format (letter(column), row(string))
    def get_pos(self, string):

        column = int( ord(string[0].upper() ) ) - 64
        row = int(string[1])

        return (row, column)


    ####################
    #  possible moves  #
    ####################

    # get all possible moves
    def get_all_possible_moves(self, game_data, move_index, real=True):
        """
            Return dictionary: Keys are piece positions and values are sets of possible positions {piece pos: {possible moves}, piece pos: {possible moves} }
        """


        possible_moves = {}
        # board = self.get_data_at_move(game_data, move_number, turn)["board"]
        # pieces = self.get_pieces(board)[color]

        # for piece in pieces:
        #     possible_moves[piece.pos] = set()
        #     for pos in board:
        #         valid = piece.is_move_valid(game_data, move_number, board, turn, self.dimensions, self.make_move, self.get_data_at_move, self.is_check, pos, real=True)
        #         if valid:
        #             possible_moves[piece.pos].add(pos)

        return possible_moves


    ###################################
    #  check / checkmate / stalemate  #
    ###################################

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
        for pos in board:
            if pos == king_pos:
                for piece in pieces[pieces_clr]:
                    valid = piece.is_move_valid(game_data, move_number, board, turn, self.dimensions, self.make_move, self.get_data_at_move, self.is_check, pos, real=False)
                    if valid:
                        return True

        return False


    # checkmate / stalemate
    def are_there_moves(self):

        if check:
            moves = self.get_all_possible_moves(game_data, move_number, turn)
            for move in moves:
                if moves[move]:
                    mate = False
                    return mate
            mate = True
        else:
            mate = False

        return mate
