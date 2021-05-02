
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
    def __init__(self, terminal):

        self.terminal = terminal
        self.spaces = " " * 14


    ###################
    #  command_input  #
    ###################

    # function manage all commands
    def command_input(self, from_where, name=""):

        usr_inp = input(f"{self.spaces}{name}@chess-terminal $ ")
        bash, parameters = self.manage_command(usr_inp)

        return self.manage_bash(bash, parameters, from_where, name)


    ##############################
    #  command_input ➔ command  #
    ##############################

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
        return list(filter(lambda par: True if par else False, command.split(" ")[1:]))


    # manage bash
    def manage_bash(self, bash, parameters, from_where, name):

        if bash == "h":
            return self.bash_help(parameters, name)
        elif bash == "m":
            return self.bash_move(parameters, from_where)
        elif bash == "col":
            return bash, parameters
        elif not bash:
            return self.command_input(from_where, name=name)
        else:
            self.terminal.invalid_bash(bash)
            return False


    ######################################
    #  command_input ➔ command ➔ bash  #
    ######################################

    # help
    def bash_help(self, parameters, name):

        if parameters:
            if parameters[0] == "m":
                self.terminal.help_move(name)
                return "h", parameters
            else:
                self.terminal.invalid_parameters("h", parameters)
                return False

        else:
            self.terminal.help_overal(name)
            return "h", parameters


    # move
    def bash_move(self, paramaters, from_where):

        if from_where == "make_move":
            if paramaters:
                if len(paramaters) == 1:
                    return "m", paramaters
                else:
                    self.terminal.too_many_parameters("m", 1)
                    return False
            else:
                self.terminal.missing_parameters("m", 1)
                return False
        else:
            self.terminal.move_no_game()
            return False


    ##############
    #  specific  #
    ##############

    # get operating system
    def specific_input(self, specifics, name=""):

        usr_inp = input(f"{self.spaces}{name}@chess-terminal $ ").strip()
        for key in specifics:
            possible_inputs = specifics[key]["exact"]
            similar_inputs = specifics[key]["similar"]

            if usr_inp in possible_inputs:
                return key
            elif usr_inp in similar_inputs:
                return self.do_you_mean(key, name)
            else:
                return False
        self.terminal.dont_recognize(usr_inp)


    # do you mean something very similar
    def do_you_mean(self, key, name):

        print(f"\n{self.bonus_spaces}Do you mean {key}? (y/n)")
        usr_inp = input(f"{self.spaces}{name}@chess-terminal $ ")

        if usr_inp == "y" or usr_inp == "yes":
            return key
        else:
            return False


    ###########
    #  other  #
    ###########

    # just press enter
    def just_enter(self, from_where, name=""):

        usr_inp = input(f"{self.spaces}{name}@chess-terminal $ ")
        bash, parameters = self.manage_command(usr_inp)

        if bash:
            return self.manage_bash(bash, parameters, from_where, name)
        else:
            return True


    # pregame data
    def just_input(self, name=""):
        return input(f"{self.spaces}{name}@chess-terminal $ ")
