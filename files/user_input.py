
#                   | main ➔ terminal
# Chess in terminal | main ➔ game_loop ➔ terminal
#                   | main ➔ game_loop ➔ game ➔ terminal

# This file manage users inputs.


###################
#  main function  #
###################

# user input
def user_input(action):

    command = input("Write your move\n $ ").split()
    bash = command[0]
    parameter = command[1]

    if bash == "m":

        if action == "move":

            return parameter



