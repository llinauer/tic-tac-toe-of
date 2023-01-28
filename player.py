"""
player.py
Author: Lukas Linauer

Player module, used for making computer moves.
Chooses its move based on a simple set of rules.

"""

BOARD_ROWS = 3
BOARD_COLS = 3


def get_available_in_row(board, row):
    """ Return positions in board(np.ndarray) of row(int) with no X or O in them"""
    positions = []
    for j in range(BOARD_COLS):
        if board[row, j] == 0:
            positions.append((row, j))
    return positions


def get_available_in_col(board, col):
    """ Return positions in board(np.ndarray) of col(int) with no X or O in them"""
    positions = []
    for i in range(BOARD_ROWS):
        if board[i, col] == 0:
            positions.append((i, col))
    return positions


def get_available_main_diagonals(board):
    """ Return diagonal positions in board(np.ndarray) with no X or O in them"""

    positions = []
    for i in range(BOARD_COLS):
        if board[i, i] == 0:
            positions.append((i, i))
    return positions


def get_available_off_main_diagonals(board):
    """ Return diagonal positions in board(np.ndarray) with no X or O in them"""

    positions = []
    for i in range(BOARD_COLS):
        if board[i, BOARD_COLS - i - 1] == 0:
            positions.append((i, i))
    return positions


def check_two_in_a_row(board, symbol):
    """ Check if there are two in a row (or column) of symbol(int) in board(np.ndarray)
        If there are, return the third position that is not occupied as a tuple (row, col) together with the symbol
        If not, return (None, None), None"""

    # loop over all rows and cols and check if there are two in a row
    # check rows
    for i in range(BOARD_ROWS):
        # two in a row of own symbol
        if sum(board[i, :]) == 2*symbol:
            return get_available_in_row(board, i)[0], symbol

        # two in a row of opponents symbol
        elif sum(board[i, :]) == -2*symbol:
            return get_available_in_row(board, i)[0], -symbol

    # check cols
    for j in range(BOARD_COLS):
        if sum(board[:, i]) == 2*symbol:
            return get_available_in_col(board, j)[0], symbol

        elif sum(board[:, i]) == -2*symbol:
            return get_available_in_col(board, j)[0], -symbol

    # check diagonals
    if sum([board[i, i] for i in range(BOARD_COLS)]) == 2*symbol:
        return get_available_main_diagonals(board)[0], symbol
    elif sum([board[i, i] for i in range(BOARD_COLS)]) == -2*symbol:
        return get_available_main_diagonals(board)[0], -symbol

    if sum([board[i, BOARD_COLS - i - 1] for i in range(BOARD_COLS)]) == 2*symbol:
        return get_available_off_main_diagonals(board)[0], symbol
    elif sum([board[i, BOARD_COLS - i - 1] for i in range(BOARD_COLS)]) == -2*symbol:
        return get_available_off_main_diagonals(board)[0], -symbol


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
