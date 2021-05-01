
# Chess in terminal | main ➔ game_loop ➔ game ➔ knight

# imports
from files.piece import Piece


##################
#  knight class  #
##################

# knight
class Knight(Piece):

    # initialize knight
    def __init__(self, player_id, pos):
        super().__init__(player_id, "knight", pos)

        self.short = {1: "", 2: "---- ", 3: "  ---", 4: " ----", 5:""}


    # is in potencial moves
    def is_in_potencial_moves(self, current_data, pos, dimensions):
        """
            Return all moves where this piece would go if board was empty
        """
        if pos != self.pos:
            if ( (pos[0] - 1 == self.pos[0] or pos[0] + 1 == self.pos[0]) and (pos[1] - 2 == self.pos[1] or pos[1] + 2 == self.pos[1]) ) or ( (pos[0] - 2 == self.pos[0] or pos[0] + 2 == self.pos[0]) and (pos[1] - 1 == self.pos[1] or pos[1] + 1 == self.pos[1]) ):
                return True


    # is it a valid move
    def is_valid(self, current_data, pos):
        """
            Check if there are any pieces between old position and new position, if not return True
        """
        if not current_data["board"][pos]:
            return True
        else:
            if current_data["board"][pos].player_id != self.player_id:
                return True
