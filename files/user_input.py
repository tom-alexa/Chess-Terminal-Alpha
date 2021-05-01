
#                   | main ➔ terminal
# Chess in terminal | main ➔ game_loop ➔ terminal ➔ user_input
#                   | main ➔ game_loop ➔ game ➔ terminal ➔ user_input

# This file manage users inputs.


#######################
#  user input object  #
#######################

# user input
class User_input():

    # initialize user input
    def __init__(self, terminal, spaces, bonus_spaces):

        self.terminal = terminal
        self.spaces = spaces
        self.bonus_spaces = bonus_spaces


    #############
    #  command  #
    #############

    # manage command
    def manage_command(self, command):
        bash, paramaters = "", []
        if command:
            bash = self.get_bash(command)
            if " " in command:
                paramaters = self.get_paramaters(command)
        return bash, paramaters

    # get bash
    def get_bash(self, command):
        return command.split(" ")[0]

    # get parameters
    def get_paramaters(self, command):
        return command.split(" ")[1:]

    # manage bash
    def manage_bash(self, bash, parameters, from_where):

        if bash == "h":
            self.bash_help(parameters)
        elif bash == "m":
            return self.bash_move(parameters, from_where)
        else:
            self.terminal.invalid_bash(bash)


    ######################
    #  different bashes  #
    ######################

    # help
    def bash_help(self, paramaters):

        if paramaters:
            if parameter[0] == "m":
                self.terminal.help_move()
            else:
                self.terminal.invalid_parameters("h", paramaters)

        else:
            self.terminal.help_overal()


    # move
    def bash_move(self, paramaters, from_where):

        if from_where == "make_move":
            if paramaters:
                if len(paramaters) == 1:
                    return True
            else:
                self.terminal.missing_parameters("m", "one")
        else:
            self.terminal.move_no_game()


    ###################
    #  move function  #
    ###################

    # user input
    def move(self, name):

        while True:
            usr_inp = input(f"{self.spaces}{name}@chess-terminal $ ")
            bash, parameters = self.manage_command(usr_inp)
            if self.manage_bash(bash, parameters, "make_move"):
                return parameters[0]



    # get operating system
    def get_operating_system(self):

        while True:
            usr_inp = input(f"\n\n{self.bonus_spaces}Write \'l\' for linux or \'w\' for windows!\n{self.spaces}@chess-terminal $ ")

            if usr_inp == "w" or usr_inp == "windows":      # windows
                return "windows"
            elif "w" in usr_inp:
                if self.do_you_mean("windows"):
                    return "windows"

            elif usr_inp == "l" or usr_inp == "linux":      # linux
                return "linux"
            elif "l" in usr_inp:
                if self.do_you_mean("linux"):
                    return "linux"


    # just press enter
    def press_enter(self):

        usr_inp = input(f"\n\n{self.bonus_spaces}Press ENTER to continue!\n{self.spaces}@chess-terminal $ ")
        bash, parameters = self.manage_command(usr_inp)
        if bash:
            self.manage_bash(bash, parameters, None)


    # pregame data
    def ask_question(self, question):
        return input(f"\n\n{self.bonus_spaces}{question}\n{self.spaces}@chess-terminal $ ")


    # do you mean something very similar
    def do_you_mean(self, what):

        while True:
            print(f"\n{self.bonus_spaces}Do you mean {what}? (y/n)")
            usr_inp = input(f"{self.spaces}@chess-terminal $ ")

            if usr_inp == "y" or usr_inp == "yes":
                return True
            elif usr_inp == "n" or usr_inp == "no":
                return False
