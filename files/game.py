
# Chess in terminal | main ➔ game_loop ➔ game

# imports
from files.king import King
from files.queen import Queen
from files.rook import Rook
from files.bishop import Bishop
from files.knight import Knight
from files.pawn import Pawn
from files.terminal import terminal_board


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
        self.dimensions = (8, 8)        # (rows, columns)
        self.playing = True
        self.board, self.string_board = self.create_board()   # return dictionary { (pos): object that is on pos}
        self.pieces = self.create_pieces()                    # return dictionary { color: {pieces} }
        self.turn = 1
        self.possible_moves = set()

        # colors
        self.colors = self.board_colors()


    # create board
    def create_board(self):

        board = {}
        # create board | { (row, column): None }
        for row in range(1, self.dimensions[0]+1):
            for column in range(1, self.dimensions[1]+1):
                board[(row, column)] = None

        string_board = ""
        return board, string_board


    # create pieces
    def create_pieces(self):
        
        # create dictionary
        pieces = {"white": set(), "black": set()}

        # both colors
        for color in ["white", "black"]:

            # pieces
            row = 1 if color == "white" else 8

            # king
            column = 5
            king = King(color, (row, column))
            pieces[color].add(king)

            # queen
            column = 4
            queen = Queen(color, (row, column))
            pieces[color].add(queen)

            # rook
            for column in [1, 8]:
                rook = Rook(color, (row, column))
                pieces[color].add(rook)

            # knight
            for column in [2, 7]:
                knight = Knight(color, (row, column))
                pieces[color].add(knight)

            # bishop
            for column in [3, 6]:
                bishop = Bishop(color, (row, column))
                pieces[color].add(bishop)

            # pawn
            row = 2 if color == "white" else 7
            for column in range(1, self.dimensions[0]+1):
                pawn = Pawn(color, (row, column))
                pieces[color].add(pawn)

        self.board = self.update_board(self.board, pieces)
        return pieces


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

        # all get possible moves
        # self.possible_moves = self.get_possible_moves(self.board, self.pieces, self.turn)

        # running while game is launched
        while self.playing:
            terminal_board(self.board, self.dimensions, self.colors)
            # move
            move = self.get_move()
            self.board, self.turn = self.make_move(self.board, self.pieces, move, self.turn)

            # check if game is finished and get all possible moves
            self.possible_moves = None
            if not self.possible_moves:
                self.playing = False


    ############
    #  phases  #
    ############

    # get move
    def get_move(self):

        # choose who will do the move
        if self.number_of_players == 2:
            move = self.player_move()
        elif self.number_of_players == 1:
            if (self.turn > 0 and self.player_color == "white") or (self.turn < 0 and self.player_color == "black"):
                move = self.player_move()
            else:
                move = self.computer_move()
        else:
            move = self.computer_move()

        return move


    # make move
    def make_move(self, board, pieces, move, turn):


        turn = self.change_turn(turn)

        return board, turn


    # get possible moves
    def get_possible_moves(self, board, pieces, turn):

        # moves that can only be played by player on the turn
        color = "white" if turn > 0 else "black"

        possible_moves = set()
        for piece in pieces[color]:
            moves = piece.get_possible_moves(board, pieces, self.dimensions)
            possible_moves.update(moves)



        return possible_moves


    ##########################
    #  move ➔ subfunctions  #
    ##########################

    # player move
    def player_move(self):

        move = "a"
        input()
        return move


    # computer move
    def computer_move(self):
        move = "ahaa"
        print(self.turn)
        return move


    # change turn after each move
    def change_turn(self, turn):
        turn *= -1
        return turn






    ############
    #  update  #
    ############

    # update board
    def update_board(self, board, pieces):
        
        # check each piece
        for color in ["white", "black"]:
            for piece in pieces[color]:
                pos = piece.pos
                board[pos] = piece

        return board
