
# Chess in terminal | main ➔ game_loop ➔ game ➔ rook

# imports
from files.piece import Piece


################
#  rook class  #
################

# rook
class Rook(Piece):

    # initialize rook
    def __init__(self, player_id, pos):
        self.short = {1: "", 2: "- - -", 3: " --- ", 4: "-----", 5: ""}
        super().__init__(player_id, "rook", pos)


    # is in potencial moves
    def is_in_potencial_moves(self, current_data, pos, dimensions):
        """
            Return all moves where this piece would go if board was empty
        """
        if pos != self.pos:
            if (pos[0] == self.pos[0]) or (pos[1] == self.pos[1]):
                return True


    # is it a valid move
    def is_valid(self, current_data, pos):
        """
            Check if there are any pieces between old position and new position, if not return True
        """
        return self.check_row_column(current_data["board"], pos)
