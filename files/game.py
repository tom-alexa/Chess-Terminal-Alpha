
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
    def __init__(self, terminal, pregame_data, dimensions=(8, 8)):

        # parameters
        self.terminal = terminal                                        # terminal where everything is printed
        self.user_input = self.terminal.user_input                      # where we get all user inputs
        self.number_of_players = pregame_data["number_of_players"]      # including either bots and human players
        self.human_players_id = pregame_data["human_players_id"]        # set contains ids of human players
        self.difficulty = pregame_data["difficulty"]                    # how difficult it is to beat the bot
        self.names = pregame_data["names"]                              # players names (bots has "BOT" before name)
        self.dimensions = dimensions                                    # (rows, columns)

        # game data
        move_number = 0                                                 # each player plays once in every turn until game is finished
        player_id = self.number_of_players - 1                          # player_id and move number are data about last move, so it is NOT saying whose turn it is NOW
        self.move_index = {"move_number": move_number, "player_id": player_id}

        # main unit (stores data about every move, if you look inside you can see data about moves you want)
        self.game_data = {move_number: {"board": self.create_board(), "castling": self.create_castling(), "check": self.create_check(), "last_pawn_move": move_number } }

        # colors
        self.colors = self.board_colors()               # data about game color, how terminal will visualize the game


    #########################
    #  initialize ➔ board  #
    #########################

    # create board with pieces on it
    def create_board(self):
        """
            Create board with self.dimension size and with pieces on it. Directory: keys are positions (row, column) and values are pieces or None
        """
        board = {}
        for row in range(1, self.dimensions[0]+1):
            for column in range(1, self.dimensions[1]+1):
                board[(row, column)] = None

        self.create_pieces(board)
        return board


    # create pieces on the board
    def create_pieces(self, board):
        """
            Create starting pieces on the board
        """
        if self.number_of_players == 2:
            for player_id in range(self.number_of_players):

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

                # rook
                for column in [1, 8]:
                    rook = Rook(player_id, (row, column))
                    board[(row, column)] = rook


                # knight
                for column in [2, 7]:
                    knight = Knight(player_id, (row, column))
                    board[(row, column)] = knight

                # bishop
                for column in [3, 6]:
                    bishop = Bishop(player_id, (row, column))
                    board[(row, column)] = bishop

                # pawn
                row = 2 if player_id == 0 else 7
                for column in range(1, self.dimensions[0]+1):
                    pawn = Pawn(player_id, (row, column))
                    board[(row, column)] = pawn


    ####################################
    #  initialize ➔ castling / check  #
    ####################################

    # create castling rights
    def create_castling(self):

        castling = {}
        for player_id in range(self.number_of_players):
            castling[player_id] = {}
            for side in range(2):   # left: 0, right: 1
                castling[player_id][side] = True

        return castling


    # create check
    def create_check(self):

        check = {}
        for player_id in range(self.number_of_players):
            check[player_id] = False

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
        """
            Main game loop
        """
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
        """
            Get move and then make it
        """
        move = self.get_move(game_data, move_index, human_players_id)   # get move
        self.make_move(game_data, move_index, move)                     # make move
        self.change_move_index(move_index)


    # return if game is finished
    def is_game_finished(self, game_data, move_index):
        """
            Tells us if game is finished
        """
        # if checkmate or stalemate
        if not self.are_there_moves(game_data, move_index, self.change_move_index(copy.deepcopy(move_index))["player_id"]):
            return True


    #########################
    #  play ➔ manage_move  #
    #########################

    # calls either computer move or player move
    def get_move(self, game_data, move_index, human_players_id):
        """
            Calls either computer move or player move, depents which turn it is
        """
        if move_index["player_id"] in human_players_id:
            move = self.player_move(game_data, move_index, self.change_move_index(copy.deepcopy(move_index))["player_id"])
        else:
            move = self.computer_move(game_data, move_index, self.change_move_index(copy.deepcopy(move_index))["player_id"])

        current_data = self.get_data_at_move(game_data, move_index)
        move["castling"] = True if self.is_castling(current_data["board"], move) else False
        move["en_passant"] = True if self.is_en_passant(current_data, move) else False

        return move


    ####################################
    #  play ➔ manage_move ➔ get_move  #
    ####################################

    # player move
    def player_move(self, game_data, move_index, player_id):
        """
            Get players input (move)
        """
        # get all possible moves
        possible_moves = self.get_all_possible_moves(game_data, move_index, player_id)

        # print board
        self.terminal.board(self.get_data_at_move(game_data, move_index), player_id, self.colors, self.dimensions)

        # get user input
        while True:


            usr_inp = False
            while not usr_inp:
                usr_inp = self.user_input.command_input("make_move", name=self.names[player_id])

            if usr_inp[0] == "m":
                try:
                    move = { "pos": {"from": self.get_pos(usr_inp[1][0][:2]), "to": self.get_pos(usr_inp[1][0][2:]) } }
                    if move["pos"]["from"] in possible_moves:
                        poss_moves_to = possible_moves[move["pos"]["from"]]
                        if move["pos"]["to"] in poss_moves_to:
                            return move
                except Exception:
                    pass
                self.terminal.specific_output(f"Move \'{usr_inp[1][0]}\' is not in possible moves!")
            else:
                if usr_inp[0] == "col":
                    self.change_colors()
                elif usr_inp[0] == "b":
                    pass
                self.terminal.board(self.get_data_at_move(game_data, move_index), player_id, self.colors, self.dimensions)


    ###################################################
    #  play ➔ manage_move ➔ get_move ➔ player_move  #
    ###################################################


    # change colors
    def change_colors(self):
        pass


    # function return position in format (row, column) form format (letter(column), row(string))
    def get_pos(self, string):
        """
            Convert user move input to the format program can take
        """
        column = int( ord(string[0].upper() ) ) - 64
        row = int(string[1])

        return (row, column)


    # tells us if given move is castling move
    def is_castling(self, board, move):
        
        if board[move["pos"]["from"]].description == "king":
            if  (move["pos"]["from"][0] == move["pos"]["to"][0]) and abs(move["pos"]["from"][1] - move["pos"]["to"][1]) == 2:
                return True


    # tells us if given move is en passant move
    def is_en_passant(self, current_data, move):

        board = current_data["board"]
        try:
            last_move = current_data["last_move"]
        except KeyError:
            return False

        if board[move["pos"]["from"]].description == "pawn":
            if move["pos"]["from"][1] != move["pos"]["to"][1]:
                if board[last_move["pos"]["to"]].description == "pawn":
                    if abs(last_move["pos"]["from"][0] - last_move["pos"]["to"][0]) == 2:
                        return True


    # computer move
    def computer_move(self, game_data, move_index, player_id):

        move = self.player_move(game_data, move_index, player_id)
        return move


    #########################
    #  play ➔ manage_move  #
    #########################

    # make move
    def make_move(self, game_data, move_index, move):
        """
            Function makes move add save new data
        """
        # current data
        current_data = copy.deepcopy(self.get_data_at_move(game_data, move_index))

        # change player_id and (if..) move number
        move_index = self.change_move_index(copy.deepcopy(move_index))
        self.add_data(game_data, current_data, move_index)

        # make actual move
        self.make_actual_move(current_data["board"], move)

        # special
        if move["castling"]:
            self.castling(current_data["board"], move)
        elif move["en_passant"]:
            self.en_passant(current_data["board"], move)

        # update current data to game data
        self.update_move(game_data, move_index, move)


    ###############################################
    #  play ➔ phases ➔ manage_move ➔ make_move  #
    ###############################################

    # increase current move index
    def change_move_index(self, move_index, up=True):
        """
            Increase or decrease move_index and return it
        """
        # new player_id and (if..) move number
        if up:
            move_index["player_id"] += 1
            if move_index["player_id"] >= self.number_of_players:
                move_index["player_id"] = 0
                move_index["move_number"] += 1
        else:
            move_index["player_id"] -= 1
            if move_index["player_id"] < 0:
                move_index["player_id"] = self.number_of_players - 1
                move_index["move_number"] -= 1
        return move_index


    # make actual move
    def make_actual_move(self, board, move):
        """
            Move piece from old position to new positionand change piece attribute pos
        """
        active_piece = copy.deepcopy(board[move["pos"]["from"]])
        active_piece.pos = move["pos"]["to"]
        board[move["pos"]["from"]] = None
        board[move["pos"]["to"]] = active_piece


    # update data about move
    def update_move(self, game_data, move_index, move):
        """
            Update data after move like "last_move", castling rights, etc.
        """
        current_data = self.get_data_at_move(game_data, move_index)
        current_data["last_move"] = move

        # active piece
        active_piece = current_data["board"][move["pos"]["to"]]

        # last pawn move
        if active_piece.description == "pawn":
            active_piece.first_move = False
            current_data["last_pawn_move"] = move_index["move_number"]

        # castling rights
        elif active_piece.description == "king":
            current_data["castling"][move_index["player_id"]] = {0: False, 1: False}

        elif active_piece.description == "rook":
            if (self.dimensions[1] + 1 - active_piece.pos[1]) >= (self.dimensions[1]//2):
                current_data["castling"][move_index["player_id"]][0] = False
            else:
                current_data["castling"][move_index["player_id"]][1] = False


        # check / checkmate / stalemate
        for player_id in range(self.number_of_players):             # for every player
            if self.is_in_check(game_data, move_index, player_id):                      # check
                current_data["check"][player_id] = True
            else:
                current_data["check"][player_id] = False


    # castling
    def castling(self, board, move):
        """
            Make move with the rook that was part of the castling
        """
        king_pos = move["pos"]["to"]

        if (self.dimensions[1] + 1 - move["pos"]["to"][1]) >= (self.dimensions[1]//2):
            self.make_actual_move(board, {"pos": {"from": (king_pos[0], 1), "to": (king_pos[0], king_pos[1] + 1) } } )                      # left
        else:
            self.make_actual_move(board, {"pos": {"from": (king_pos[0], self.dimensions[1]), "to": (king_pos[0], king_pos[1] - 1) } } )     # right


    # en passant
    def en_passant(self, board, move):
        """
            Delete pawn which was "en passanted" from the board
        """
        board[(move["pos"]["from"][0], move["pos"]["to"][1])] = None


    # add certain data in the game data
    def add_data(self, game_data, current_data, move_index):
        """
            Add certain data in the game data
        """
        if move_index["player_id"] == 0:
            game_data[move_index["move_number"]] = {move_index["player_id"]: current_data}
        else:
            game_data[move_index["move_number"]][move_index["player_id"]] = current_data


    ###################
    #  get something  #
    ###################

    # find king/queen/rook/bishop/knight/pawn position
    def find_pos_of_piece(self, piece_desc, board, player_id):
        """
            Return set of positions of given kind of piece
        """
        positions = []
        for pos in board:
            if board[pos]:
                if board[pos].description == piece_desc and board[pos].player_id == player_id:
                    positions.append(pos)
        
        return positions


    # function return all pieces which belongs to the given player id
    def get_pieces(self, board, player_id):
        """
            Return of all pieces that belong to the given player
        """
        pieces = set()
        for pos in board:
            if board[pos]:
                if board[pos].player_id == player_id:
                    pieces.add(board[pos])

        return pieces


    # return data at exact moment
    def get_data_at_move(self, game_data, move_index):
        """
            Return data at exact moment
        """
        if move_index["move_number"] > 0:
            return game_data[move_index["move_number"]][move_index["player_id"]]
        else:
            return game_data[move_index["move_number"]]


    ####################
    #  possible moves  #
    ####################

    # get all possible moves
    def get_all_possible_moves(self, game_data, move_index, player_id):
        """
            Return dictionary: Keys are piece positions and values are sets of possible positions {piece pos: {possible moves}, piece pos: {possible moves} }
        """
        possible_moves = {}
        pieces = self.get_pieces(self.get_data_at_move(game_data, move_index)["board"], player_id)
        for piece in pieces:
            possible_moves[piece.pos] = set()

        for pos in self.get_data_at_move(game_data, move_index)["board"]:
            attack_pieces = self.who_attack(game_data, move_index, pieces, pos)
            for piece in attack_pieces:
                possible_moves[piece.pos].add(pos)

        return possible_moves


    # who attack on exact position
    def who_attack(self, game_data, move_index, pieces, attack_pos, check_matter=True):
        """
            Return set of pieces which attack exact position
        """
        attack_pieces = set()
        for piece in pieces:
            if piece.is_move_possible(game_data, move_index, attack_pos, check_matter, self.dimensions, is_in_check=self.is_in_check, make_move=self.make_move, is_castling=self.is_castling, is_en_passant=self.is_en_passant, get_data_at_move=self.get_data_at_move, change_move_index=self.change_move_index):
                attack_pieces.add(piece)

        return attack_pieces


    ###################################
    #  check / checkmate / stalemate  #
    ###################################

    # detect check
    def is_in_check(self, game_data, move_index, player_id):
        """
            Return boolean value if player is in check
        """
        current_data = self.get_data_at_move(game_data, move_index)
        king_pos = current_data["board"][self.find_pos_of_piece("king", current_data["board"], player_id)[0]].pos

        pieces = set()
        for p_id in range(self.number_of_players):
            if p_id != player_id:
                pieces.update(self.get_pieces(current_data["board"], p_id))

        if self.who_attack(game_data, move_index, pieces, king_pos, check_matter=False):
            return True


    # checkmate / stalemate
    def are_there_moves(self, game_data, move_index, player_id):
        """
            Return boolean value if player is in checkmate / stalemate (depends if is in check)
        """

        all_poss_moves = self.get_all_possible_moves(game_data, move_index, player_id)
        for piece in all_poss_moves:
            if all_poss_moves[piece]:
                return True
        return False
