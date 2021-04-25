
# Chess in terminal | main.py ➔ game_loop.py

# imports
from files.game import Game


###############
#  game loop  #
###############

# game loop
def game_loop():
    
    # running in while loop, if game is finished ask for another one
    running = True
    while running:

        # ask user for data (how many players, difficulty, players names)
        game_data = get_starting_data()  # return dictionary

        # game object
        game = Game(game_data["number of players"], game_data["difficulty"], game_data["names"])
        game.play()

        # game conclusion (who wins etc.)
        game_ending()


############
#  phases  #
############

# ask user for starting data
def get_starting_data():

    # creating data dictionary
    game_data = {}
    game_data["number of players"] = None
    game_data["difficulty"] = None
    game_data["names"] = None

    return game_data


# game conclusion
def game_ending():
    pass