
# Chess in terminal | main ➔ game_loop

# imports
from files.game import Game


###############
#  game loop  #
###############

# game loop
def game_loop(terminal):
    
    # running in while loop, if game is finished ask for another one
    running = True
    while running:

        # ask user for data (how many players, difficulty, players names)
        pregame_data = get_starting_data(terminal)

        # game object
        game = Game(terminal, pregame_data)
        game.play()

        # game conclusion (who wins etc.)
        game_ending()

        # ask if user want to play again
        running = play_again()


############
#  phases  #
############

# ask user for starting data
def get_starting_data(terminal):

    # creating data dictionary
    terminal.reset_window()
    game_data = {"number_of_players": 2, "human_players_id": get_human_players(terminal)}
    game_data["difficulty"] = get_difficulty(terminal) if len(game_data["human_players_id"]) == 1 else None
    game_data["names"] = get_players_names(terminal, game_data["human_players_id"])

    return game_data


# game conclusion
def game_ending():
    pass


# ask if user want to play again
def play_again():

    return False


########################
#  phases ➔ get data  #
########################

# human players
def get_human_players(terminal):

    while True:
        terminal.specific_output("How many players are going to play?")
        usr_inp = terminal.user_input.just_input()
        try:
            n = int(usr_inp)
            if n == 1:
                return get_human_id(terminal)
            elif n == 2:
                return {0, 1}
            else:
                terminal.specific_output("Write number {0;1;2}!")
        except ValueError:
            terminal.specific_output("Write number {0;1;2}!")


# get human id
def get_human_id(terminal):

    while True:
        terminal.specific_output("Do you want to be white \'0\' or black \'1\'?")
        usr_inp = terminal.user_input.just_input()
        try:
            n = int(usr_inp)
            if n == 0 or n == 1:
                return {n}
            else:
                terminal.specific_output("Write number {0;1}!")
        except ValueError:
            terminal.specific_output("Write number {0;1}!")


# get diffuculty
def get_difficulty(terminal):

    while True:
        terminal.specific_output("How good your opponent should be? (1-worst; 5-best)")
        usr_inp = terminal.user_input.just_input()
        try:
            n = int(usr_inp)
            if n == 1 or n == 2 or n == 3 or n == 4 or n == 5:
                return n
            else:
                terminal.specific_output("Write number \{1-5\}!")
        except ValueError:
            terminal.specific_output("Write number {1-5}!")


# get players names
def get_players_names(terminal, players):

    names = {}
    for player in players:
        terminal.specific_output(f"What is name of player {player}?")
        usr_inp = terminal.user_input.just_input()
        names[player] = usr_inp
    return names
