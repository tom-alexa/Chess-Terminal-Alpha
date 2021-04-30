
#                   | main ➔ terminal
# Chess in terminal | main ➔ game_loop ➔ terminal ➔ user_input
#                   | main ➔ game_loop ➔ game ➔ terminal ➔ user_input

# This file manage users inputs.


#######################
#  user input object  #
#######################

# user input
class User_input():

    ###################
    #  main function  #
    ###################

    # user input
    def main(self, action):

        spaces = " " * 10
        usr_inp = input(f"{spaces}@chess-terminal $ ").split()
        lenght = len(usr_inp)

        if action == "move":
            self.move()

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

    # get operating system
    def get_operating_system(self):

        return "w"

    def move(self):
        move_input = ""
        if move_input == "no command" or move_input == "no parameter" or move_input == "unknown command":
            print(move_input)
        return move_input

