
#                   | main ➔ terminal
# Chess in terminal | main ➔ game_loop ➔ terminal
#                   | main ➔ game_loop ➔ game ➔ terminal

# This file manage users inputs.

# imports
from files.terminal import main_terminal


###################
#  main function  #
###################

# user input
def user_input(action):

    spaces = " " * 10
    usr_inp = input(f"{spaces}@chess-terminal $ ").split()
    lenght = len(usr_inp)




    if lenght >= 1:
        command = usr_inp[0]


        if action == "operating system":
            if command == "w" or command == "windows":
                return "windows"
            elif command == "l" or command == "linux":
                return "linux"
            else:
                return "unknown"


        if command == "m":
            if action == "move":
                if lenght > 1:
                    parameter = usr_inp[1]
                    return parameter
                else:
                    return "no parameter"
            else:
                return "no move"

        elif command == "h":
            main_terminal("help")
            return user_input(action)

        else:
            return "unknown command"

    else:
        return "no command"

