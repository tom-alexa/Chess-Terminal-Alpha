
# Chess in terminal | main ➔ game_loop ➔ game ➔ pawn

# imports
from files.piece import Piece


################
#  pawn class  #
################

# pawn
class Pawn(Piece):

    # initialize pawn
    def __init__(self, player_id, pos):
        super().__init__(player_id, "pawn", pos)

        self.short = {1: "", 2: "", 3: "  -  ", 4: " --- ", 5:""}
        self.first_move = True


    # is in potencial moves
    def is_in_potencial_moves(self, current_data, pos, dimensions):
        """
            Return all moves where this piece would go if board was empty
        """
        step = 1 if self.player_id == 0 else -1
        if pos != self.pos:
            if (pos[0] == self.pos[0] + step):
                if (pos[0] == self.pos[0] + step) and ( (pos[1] == self.pos[1]) or (pos[1] == self.pos[1] + 1) or (pos[1] == self.pos[1] - 1 ) ):
                    return True
            elif (pos[0] == self.pos[0] + (2*step)) and (self.first_move) and (pos[1] == self.pos[1]):      # first two square move
                return True


    # is it a valid move
    def is_valid(self, current_data, pos):
        """
            Check if there are any pieces between old position and new position, if not return True
        """
        if pos[1] == self.pos[1]:                       # move one step forward
            return self.check_row_column(current_data["board"], pos)
        else:
            try:                                        # pawn takes diagonaly
                last_move = current_data["last_move"]
            except KeyError:
                last_move = None

            return self.check_diagonal(current_data["board"], pos, last_move)

