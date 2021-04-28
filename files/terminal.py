
#                   | main ➔ terminal
# Chess in terminal | main ➔ game_loop ➔ terminal
#                   | main ➔ game_loop ➔ game ➔ terminal

# Basically you call what you want to print in terminal.

# imports
import os


###############
#  constants  #
###############

RESET = "\u001b[0m"
BLANK_LINE = "\n"




###########
#  board  #
###########

# terminal board
def terminal_board(board, dimensions, colors):

    #####################
    #  marks (letters)  #
    #####################

    def add_letters(string):

        line = {1: "", 2: "", 3: "", 4: "", 5:""}
        for i in line:
            for column in range(dimensions[1]+1):
                if column < 1:
                    line[i] += (" " * 19)

                else:
                    desc = letters[column][i]
                    bg = RESET

                    if desc:
                        clr = RESET

                        for _ in range(2):
                            line[i] = square_symbol(line[i], bg, " ")

                        for place_in_desc in desc:
                            if place_in_desc != " ":
                                line[i] = square_symbol(line[i], clr, place_in_desc)
                            else:
                                line[i] = square_symbol(line[i], bg, " ")

                        for _ in range(2):
                            line[i] = square_symbol(line[i], bg, " ")

            string += line[i] + RESET + BLANK_LINE

        return string
    

    string_board = BLANK_LINE

    pl_1_col = get_ascii_color(colors["pl_1"])
    pl_2_col = get_ascii_color(colors["pl_2"])
    bg_1 = get_ascii_color(colors["bg_1"], backgound=True)
    bg_2 = get_ascii_color(colors["bg_2"], backgound=True)

    numbers = create_numbers(dimensions[0])
    letters = create_letters(dimensions[1])


    string_board = add_letters(string_board)

    for row in range(dimensions[0], 0, -1):
        line = {1: "", 2: "", 3: "", 4: "", 5:""}

        for i in line:
            string_board += (" " * 10)

            for column in range(dimensions[1]+2):


                #####################
                #  marks (numbers)  #
                #####################

                if column < 1 or column > dimensions[1]:
                    desc = numbers[row][i]
                    bg = RESET

                    if desc:
                        clr = RESET

                        for _ in range(2):
                            line[i] = square_symbol(line[i], bg, " ")

                        for place_in_desc in desc:
                            if place_in_desc != " ":
                                line[i] = square_symbol(line[i], clr, place_in_desc)
                            else:
                                line[i] = square_symbol(line[i], bg, " ")

                        for _ in range(2):
                            line[i] = square_symbol(line[i], bg, " ")

                    else:
                        for _ in range(9):
                            line[i] = square_symbol(line[i], bg, " ")


                ################
                #  chessboard  #
                ################

                else:
                    piece = board[(row, column)]
                    bg = bg_1 if (row + column) % 2 == 0 else bg_2

                    if piece:
                        desc = piece.short[i]

                        if desc:
                            clr = pl_1_col if piece.color == "white" else pl_2_col

                            for _ in range(2):
                                line[i] = square_symbol(line[i], bg, " ")

                            for place_in_desc in desc:
                                if place_in_desc != " ":
                                    line[i] = square_symbol(line[i], clr, "█")
                                else:
                                    line[i] = square_symbol(line[i], bg, " ")

                            for _ in range(2):
                                line[i] = square_symbol(line[i], bg, " ")

                        else:
                            for _ in range(9):
                                line[i] = square_symbol(line[i], bg, " ")

                    else:
                        for _ in range(9):
                            line[i] = square_symbol(line[i], bg, " ")

            string_board += line[i] + RESET + BLANK_LINE

    string_board = add_letters(string_board)


    # print board on the screen
    os.system("mode con: cols=120 lines=60")
    print(string_board)


# just print symbol with added background
def square_symbol(string, color, symbol):

    string += color + symbol

    return string





# function return color as ascii symbol
def get_ascii_color(color, backgound=False):

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
def create_letters(rows):

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
def create_numbers(columns):
    
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
