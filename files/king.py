
# Chess in terminal | main ➔ game_loop ➔ game ➔ king

# imports
from files.piece import Piece


################
#  king class  #
################

# king
class King(Piece):

    # initialize king
    def __init__(self, player_id, pos):
        super().__init__(player_id, "king", pos)

        self.short = {1: "", 2: " --- ", 3: "- - -", 4: "-----", 5:""}


    # is in potencial moves
    def is_in_potencial_moves(self, current_data, pos, dimensions):
        """
            Return all moves where this piece would go if board was empty
        """
        if pos != self.pos:
            if (pos[0] == self.pos[0] - 1) or (pos[0] == self.pos[0]) or (pos[0] == self.pos[0] + 1):               # one square far
                if (pos[1] == self.pos[1] - 1) or (pos[1] == self.pos[1]) or (pos[1] == self.pos[1] + 1):
                    return True
                elif current_data["castling"][0] and (pos[0] == self.pos[0]) and (pos[1] == self.pos[1] - 2):       # two square far if castling
                    return True
                elif current_data["castling"][1] and (pos[0] == self.pos[0]) and (pos[1] == self.pos[1] + 2):
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
