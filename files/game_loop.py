
# Chess in terminal | main ➔ game_loop

# imports
from files.game import Game


###############
#  game loop  #
###############

# game loop
def game_loop(op_sys):
    
    # running in while loop, if game is finished ask for another one
    running = True
    while running:

        # ask user for data (how many players, difficulty, players names)
        game_data = get_starting_data()  # return dictionary

        # game object
        game = Game(game_data["number of players"], game_data["difficulty"], game_data["names"], game_data["player color"], op_sys)
        game.play()

        # game conclusion (who wins etc.)
        game_ending()

        # ask if user want to play again
        running = play_again()


############
#  phases  #
############

# ask user for starting data
def get_starting_data():

    # creating data dictionary
    game_data = {}
    game_data["number of players"] = 1
    game_data["difficulty"] = None
    game_data["names"] = None
    game_data["player color"] = "white"

    return game_data


# game conclusion
def game_ending():
    pass


# ask if user want to play again
def play_again():

    return False
