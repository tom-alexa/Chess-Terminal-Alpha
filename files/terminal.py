
#                   | main ➔ terminal
# Chess in terminal | main ➔ game_loop ➔ terminal
#                   | main ➔ game_loop ➔ game ➔ terminal

# Basically you call what you what to print in terminal.

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
    
    dashes = "-" * (3 * dimensions[1])
    string_board = BLANK_LINE

    pl_1_col = get_ascii_color(colors["pl_1"])
    pl_2_col = get_ascii_color(colors["pl_2"])
    bg_1 = get_ascii_color(colors["bg_1"], backgound=True)
    bg_2 = get_ascii_color(colors["bg_2"], backgound=True)


    for row in range(1, dimensions[0]+1):
        line = {1: "", 2: "", 3: "", 4: "", 5:""}

        for i in line:
            string_board += "    "

            for column in range(1, dimensions[1]+1):
                piece = board[(row, column)]
                bg = bg_1 if (row + column) % 2 == 0 else bg_2

                if piece:
                    desc = piece.short[i]

                    if desc:
                        clr = pl_1_col if piece.color == "white" else pl_2_col

                        for _ in range(2):
                            line[i] = square_symbol(line[i], bg)

                        for place_in_desc in desc:
                            if place_in_desc != " ":
                                line[i] = square_symbol(line[i], clr, blank=False)
                            else:
                                line[i] = square_symbol(line[i], bg)

                        for _ in range(2):
                            line[i] = square_symbol(line[i], bg)

                    else:
                        for _ in range(9):
                            line[i] = square_symbol(line[i], bg)

                else:
                    for _ in range(9):
                        line[i] = square_symbol(line[i], bg)

            string_board += line[i] + RESET + BLANK_LINE

    # print board on the screen
    os.system("mode con: cols=80 lines=60")
    print(string_board)


# just print symbol with added background
def square_symbol(string, color, blank=True):

    symbol = " " if blank else "█"
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
