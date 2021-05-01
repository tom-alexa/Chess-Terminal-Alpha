
# Chess in terminal | main ➔ game_loop ➔ game ➔ queen

# imports
from files.piece import Piece


#################
#  queen class  #
#################

# queen
class Queen(Piece):

    # initialize queen
    def __init__(self, player_id, pos):
        super().__init__(player_id, "queen", pos)

        self.short = {1: "", 2: " - - ", 3: "-----", 4: " --- ", 5: ""}


    # is in potencial moves
    def is_in_potencial_moves(self, current_data, pos, dimensions):
        """
            Return all moves where this piece would go if board was empty
        """
        if pos != self.pos:
            if (pos[0] == self.pos[0]) or (pos[1] == self.pos[1]) or (pos[0] - pos[1] == self.pos[0] - self.pos[1]) or ( (dimensions[0] - pos[0]) - pos[1] == (dimensions[0] - self.pos[0]) - self.pos[1] ):
                return True


    # is it a valid move
    def is_valid(self, current_data, pos):
        """
            Check if there are any pieces between old position and new position, if not return True
        """
        if pos[0] == self.pos[0] or pos[1] == self.pos[1]:
            return self.check_row_column(current_data["board"], pos)
        else:
            return self.check_diagonal(current_data["board"], pos)
