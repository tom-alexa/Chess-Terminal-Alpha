
# Chess in terminal | main ➔ game_loop ➔ game

# imports
from files.king import King
from files.queen import Queen
from files.rook import Rook
from files.bishop import Bishop
from files.knight import Knight
from files.pawn import Pawn


#################
#  game object  #
#################

# game
class Game():

    # initial game
    def __init__(self, number_of_players, difficulty, names):

        # parameters
        self.number_of_players = number_of_players
        self.difficulty = difficulty
        self.names = names

        # variables
        self.dimensions = (8, 8)            # (rows, columns)
        self.playing = True
        self.board = self.create_board()    # return dictionary { (pos): object that is on pos}
        self.pieces = self.create_pieces()  # return dictionary { color: [pieces] }
        print(self.pieces)
        self.turn = 1


    # create board
    def create_board(self):

        board = {}
        # create board | { (row, column): None }
        for row in range(1, self.dimensions[0]+1):
            for column in range(1, self.dimensions[1]+1):
                board[(row, column)] = None

        return board


    # create pieces
    def create_pieces(self):
        
        # create dictionary
        pieces = {"white": [], "black": []}

        # both colors
        for color in ["white", "black"]:

            # pieces
            row = 1 if color == "white" else 8

            # king
            column = 5
            king = King(color, (row, column))
            pieces[color].append(king)

            # queen
            column = 4
            queen = Queen(color, (row, column))
            pieces[color].append(queen)

            # rook
            for column in [1, 8]:
                rook = Rook(color, (row, column))
                pieces[color].append(rook)

            # knight
            for column in [2, 7]:
                knight = Knight(color, (row, column))
                pieces[color].append(knight)

            # bishop
            for column in [3, 6]:
                bishop = Bishop(color, (row, column))
                pieces[color].append(bishop)

            # pawn
            row = 2 if color == "white" else 7
            for column in range(1, self.dimensions[0]+1):
                pawn = Pawn(color, (row, column))
                pieces[color].append(pawn)

        self.__update_board(self.board, pieces)
        return pieces


    ##########
    #  play  #
    ##########

    # play (this is where actual game is happening)
    def play(self):

        # running while game is launched
        while self.playing:

            self.move()              # make move
            self.check_playing()     # check if game is finished


    ############
    #  phases  #
    ############

    # make move
    def move(self):
        pass


    # check if game is finished
    def check_playing(self):
        pass


    ##########################
    #  move ➔ subfunctions  #
    ##########################

    # change turn after each move
    def change_turn(self):
        self.turn *= -1


    #############
    #  private  #
    #############

    # update board
    def __update_board(self, board, pieces):
        
        # check each piece
        for color in ["white", "black"]:
            for piece in pieces[color]:
                pos = piece.pos
                board[pos] = piece
