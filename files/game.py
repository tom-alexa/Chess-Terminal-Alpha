
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
        self.pieces = self.create_pieces()                    # return dictionary { color: [pieces] }
        self.turn = 1


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

        self.board, self.string_board = self.update_board(self.board, pieces)
        return pieces


    ##########
    #  play  #
    ##########

    # play (this is where actual game is happening)
    def play(self):

        # running while game is launched
        while self.playing:

            move = self.get_move()      # choose move
            self.board, self.turn = self.make_move(self.board, move, self.turn)     # make move
            self.playing = self.check_playing(self.board, self.turn)                # check if game is finished


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
    def make_move(self, board, move, turn):


        turn = self.change_turn(turn)

        return board, turn


    # check if game is finished
    def check_playing(self, board, turn):
        
        return True


    ##########################
    #  move ➔ subfunctions  #
    ##########################

    # player move
    def player_move(self):
        move = "aha"
        print(self.turn)
        print(self.string_board)
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

        # string board
        dashes = "-" * (5 * self.dimensions[1] + 1)
        string_board = f"    {dashes}"

        for row in range(1, self.dimensions[0]+1):
            string_board += "\n    |"
            for column in range(1, self.dimensions[1]+1):
                piece = board[(row, column)]
                if piece:
                    short = piece.short
                    string_board += f" {short} |"
                else:
                    string_board += "    |"

            string_board += f"\n    {dashes}"

        return board, string_board
