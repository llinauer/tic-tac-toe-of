"""
player.py
Author: Lukas Linauer

Player module, used for making computer moves.
Chooses its move based on a simple set of rules.

"""

BOARD_ROWS = 3
BOARD_COLS = 3

from state import get_available_in_row, get_available_in_col


def check_two_in_a_row(board, symbol):
    """ Check if there are two in a row (or column) of symbol(int) in board(np.ndarray)
        If there are, return the third position that is not occupied as a tuple (row, col)
        If not, return (None, None)"""

    # loop over all rows and cols and check if there are two in a row
    # check rows
    for i in range(BOARD_ROWS):
        if sum(board[i, :]) == 2*symbol:
            return get_available_in_row(board, row)

        elif sum(board[i, :]) == -2:
            self.is_end = True
            return -1

    # check cols
    for i in range(BOARD_COLS):
        if sum(self.board[:, i]) == 3:
            self.is_end = True
            return 1
        elif sum(self.board[:, i]) == -3:
            self.is_end = True
            return -1

    # check diagonals
    diag_sum1 = sum([self.board[i, i] for i in range(BOARD_COLS)])
    diag_sum2 = sum([self.board[i, BOARD_COLS - i - 1] for i in range(BOARD_COLS)])



class Player:
    """Player class"""

    def __init__(self, name, human=False):
        """init method"""

        self.name = name
        self.states = []  # states is a list of coordinate tuples (e.g. [(0,0), (0,2), ...]
        self.human = human


    def choose_action(self, positions, current_board, symbol):
        """Choose action for the player based on the available positions (list) on the current_board (np.array)
           symbol is either 1 for player 1 or -1 for player 2
           return which action(tuple) should be taken"""

        # Rules for perfect play: https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy
        # Rule 1: If you have two in a row, place the third to win



        return action
