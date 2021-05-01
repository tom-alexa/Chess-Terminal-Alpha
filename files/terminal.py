
#                   | main ➔ terminal
# Chess in terminal | main ➔ game_loop ➔ terminal
#                   | main ➔ game_loop ➔ game ➔ terminal

# Basically you call what you want to print in terminal.

# imports
import os
from files.user_input import User_input


####################
#  Terminal class  #
####################

# terminal
class Terminal():

    # initialize terminal
    def __init__(self):

        # spaces from the left
        self.spaces = " " * 14
        self.bonus_spaces = " " * 10

        self.user_input = User_input(self, self.spaces, self.bonus_spaces)
        self.operating_system = self.user_input.get_operating_system()
        self.RESET = "\u001b[0m"
        self.BLANK_LINE = "\n"


    #############################
    #  introduction and ending  #
    #############################

    # introduction
    def introduction(self):

        self.reset_window()

        spaces_from_left = 40
        name = "Chess - terminal"
        author = "by Tom Alexa"
        spaces_between = (len(name) - len(author))//2

        spaces = " " * spaces_from_left
        print(f"\n\n\n\n\n{spaces}{name}")

        spaces = " " * (spaces_from_left + spaces_between)
        print(f"\n{spaces}{author}\n\n")

        spaces = " " * (spaces_from_left + 2)
        print(f"\n{spaces}HOW TO PLAY")

        spaces = " " * (spaces_from_left - 10)
        print(f"\n{spaces}The game works on basis of commands.\n")

        spaces = " " * (spaces_from_left - 5)
        print(f"{spaces}$ h             (print all commands)")
        print(f"{spaces}$ h \'command\'   (print info about command)")
        print(f"{spaces}$ m \'move\'      (make move)")

        self.user_input.press_enter()


    ###########
    #  board  #
    ###########

    # print board
    def board(self, current_data, player_id, colors, dimensions):

        # reset window
        self.reset_window()

        board = current_data["board"]
        check = current_data["check"][player_id]

        # spaces from left side
        spaces_from_left = 5

        # create string
        string_board = ""

        pl_1_col = self.get_ascii_color(colors["pl_1"])
        pl_2_col = self.get_ascii_color(colors["pl_2"])
        bg_1 = self.get_ascii_color(colors["bg_1"], backgound=True)
        bg_2 = self.get_ascii_color(colors["bg_2"], backgound=True)

        numbers = self.create_numbers(dimensions[0])

        string_board = self.add_letters(string_board, dimensions, spaces_from_left)

        for row in range(dimensions[0], 0, -1):
            line = {1: "", 2: "", 3: "", 4: "", 5:""}

            for i in line:
                string_board += (" " * spaces_from_left)

                for column in range(dimensions[1]+2):

                    #####################
                    #  marks (numbers)  #
                    #####################

                    if column < 1 or column > dimensions[1]:
                        desc = numbers[row][i]
                        bg = self.RESET

                        if desc:
                            clr = self.RESET

                            for _ in range(2):
                                line[i] = self.square_symbol(line[i], bg, " ")

                            for place_in_desc in desc:
                                if place_in_desc != " ":
                                    line[i] = self.square_symbol(line[i], clr, place_in_desc)
                                else:
                                    line[i] = self.square_symbol(line[i], bg, " ")

                            for _ in range(2):
                                line[i] = self.square_symbol(line[i], bg, " ")

                        else:
                            for _ in range(9):
                                line[i] = self.square_symbol(line[i], bg, " ")


                    ################
                    #  chessboard  #
                    ################

                    else:
                        piece = board[(row, column)]
                        bg = bg_1 if (row + column) % 2 == 0 else bg_2

                        if piece:
                            desc = piece.short[i]

                            if desc:
                                clr = pl_1_col if piece.player_id == player_id else pl_2_col

                                for _ in range(2):
                                    line[i] = self.square_symbol(line[i], bg, " ")

                                for place_in_desc in desc:
                                    if place_in_desc != " ":
                                        line[i] = self.square_symbol(line[i], clr, "█")
                                    else:
                                        line[i] = self.square_symbol(line[i], bg, " ")

                                for _ in range(2):
                                    line[i] = self.square_symbol(line[i], bg, " ")

                            else:
                                for _ in range(9):
                                    line[i] = self.square_symbol(line[i], bg, " ")

                        else:
                            for _ in range(9):
                                line[i] = self.square_symbol(line[i], bg, " ")

                string_board += line[i] + self.RESET + self.BLANK_LINE

        string_board = self.add_letters(string_board, dimensions, spaces_from_left)
        string_board = string_board[:-1]

        # print board on the screen
        print(string_board)
        if check:
            print("!!! CHECK !!!")


    #####################
    #  marks (letters)  #
    #####################

    def add_letters(self, string, dimensions, spaces_from_left):

        letters = self.create_letters(dimensions[1])

        line = {1: "", 2: "", 3: "", 4: "", 5:""}
        for i in line:
            for column in range(dimensions[1]+1):
                if column < 1:
                    line[i] += (" " * ( spaces_from_left+9) )

                else:
                    desc = letters[column][i]
                    bg = self.RESET

                    if desc:
                        clr = self.RESET

                        for _ in range(2):
                            line[i] = self.square_symbol(line[i], bg, " ")

                        for place_in_desc in desc:
                            if place_in_desc != " ":
                                line[i] = self.square_symbol(line[i], clr, place_in_desc)
                            else:
                                line[i] = self.square_symbol(line[i], bg, " ")

                        for _ in range(2):
                            line[i] = self.square_symbol(line[i], bg, " ")

            string += line[i] + self.RESET + self.BLANK_LINE

        return string


    # just print symbol with added background
    def square_symbol(self, string, color, symbol):

        string += color + symbol
        return string


    # function return color as ascii symbol
    def get_ascii_color(self, color, backgound=False):

        # eighter it is background or not
        b_sym = "4" if backgound else "3"

        if color == "black":
            ascii_color = f"\u001b[{b_sym}0m"
        elif color == "red":
            ascii_color = f"\u001b[{b_sym}1m"
        elif color == "green":
            ascii_color = f"\u001b[{b_sym}2m"
        elif color == "yellow":
            ascii_color = f"\u001b[{b_sym}3m"
        elif color == "blue":
            ascii_color = f"\u001b[{b_sym}4m"
        elif color == "magenta":
            ascii_color = f"\u001b[{b_sym}5m"
        elif color == "cyan":
            ascii_color = f"\u001b[{b_sym}6m"
        elif color == "white":
            ascii_color = f"\u001b[{b_sym}7m"

        return ascii_color


    # create letter
    def create_letters(self, columns):

        letters = {}
        letters[1] = {1: "", 2: " ┌─┐ ", 3: "┌┴─┴┐", 4: "┴   ┴", 5: ""}
        letters[2] = {1: "", 2: "╓───┐", 3: "║───┤", 4: "╙───┘", 5: ""}
        letters[3] = {1: "", 2: "╓─── ", 3: "║    ", 4: "╙─── ", 5: ""}
        letters[4] = {1: "", 2: "╓───┐", 3: "║   │", 4: "╙───┘", 5: ""}
        letters[5] = {1: "", 2: "╓─── ", 3: "║─── ", 4: "╙─── ", 5: ""}
        letters[6] = {1: "", 2: "╓─── ", 3: "║─── ", 4: "╩    ", 5: ""}
        letters[7] = {1: "", 2: "╓───┐", 3: "║  ─┐", 4: "╙───┘", 5: ""}
        letters[8] = {1: "", 2: "╦   ╦", 3: "║───╢", 4: "╩   ╩", 5: ""}

        return letters


    # create numbers
    def create_numbers(self, rows):

        numbers = {}
        numbers[1] = {1: "", 2: " ┌┐  ", 3: "  │  ", 4: " ─┴─ ", 5: ""}
        numbers[2] = {1: "", 2: " ┌─┐ ", 3: " ┌─┘ ", 4: " └── ", 5: ""}
        numbers[3] = {1: "", 2: " ──┐ ", 3: " ──┤ ", 4: " ──┘ ", 5: ""}
        numbers[4] = {1: "", 2: " ┬ ┬ ", 3: " └─┼─", 4: "   ┴ ", 5: ""}
        numbers[5] = {1: "", 2: " ┌── ", 3: " └─┐ ", 4: " └─┘ ", 5: ""}
        numbers[6] = {1: "", 2: " ┌─┐ ", 3: " ├─┐ ", 4: " └─┘ ", 5: ""}
        numbers[7] = {1: "", 2: " ──┐ ", 3: "  ┌┘ ", 4: " ─┴─ ", 5: ""}
        numbers[8] = {1: "", 2: " ┌─┐ ", 3: " ├─┤ ", 4: " └─┘ ", 5: ""}

        return numbers


    ##############
    #  manually  #
    ##############

    # write manually
    def manually(self, sentence):
        print(f"\n{self.bonus_spaces}{sentence}\n")


    ######################
    #  commands ➔ help  #
    ######################

    # main help
    def help_overal(self):

        self.reset_window()
        print("overal help")
        self.user_input.press_enter()


    # move help
    def help_move(self):

        self.reset_window()
        print("move help")
        self.user_input.press_enter()


    ######################
    #  commands ➔ move  #
    ######################

    # there is no game to make move
    def move_no_game(self):

        print("You have to start game first!")


    #########################
    #  commands ➔ invalid  #
    #########################

    # invalid bash
    def invalid_bash(self, bash):

        print(f"invalid bash \'{bash}\'")


    # invalid parameters
    def invalid_parameters(self, bash, paramaters):

        paramaters_string = " ".join(paramaters)
        print(f"bash {bash} has no parameter(s) {paramaters_string}")


    # missing parameters
    def missing_parameters(self, bash, number):
        print(f"bash {bash} require {number} parameter(s)")


    ###########
    #  reset  #
    ###########

    # reset window
    def reset_window(self):

        # clean window
        if self.operating_system == "windows":
            os.system("cls")
        elif self.operating_system == "linux":
            os.system("clear")

        # new window size
        os.system("mode con: cols=100 lines=52")
