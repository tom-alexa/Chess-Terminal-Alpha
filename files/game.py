
# Chess in terminal | main.py ➔ game_loop.py ➔ game.py


#################
#  game object  #
#################

# game
class Game():

    # initial game
    def __init__(self, number_of_players, difficulty, names):

        # parameters
        self.number_of_players = number_of_players
        self.difficulty = difficulty
        self.names = names

        # variables
        self.playing = True


    # play (this is where actual game is happening)
    def play(self):

        # running while game is launched
        while self.playing:

            self.move()              # make move
            self.check_playing()     # check if game is finished


    ############
    #  phases  #
    ############

    # make move
    def move(self):
        pass


    # check if game is finished
    def check_playing(self):
        pass
