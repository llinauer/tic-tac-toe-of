"""
player.py
Author: Lukas Linauer

Player module, used for making computer moves.
Chooses its move based on a simple set of rules.

"""

BOARD_ROWS = 3
BOARD_COLS = 3

import numpy as np


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
            positions.append((i, BOARD_COLS -i - 1))
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
            return get_available_in_row(board, i)[0]

    # check cols
    for j in range(BOARD_COLS):
        if sum(board[:, j]) == 2*symbol:
            return get_available_in_col(board, j)[0]

    # check diagonals
    if sum([board[i, i] for i in range(BOARD_COLS)]) == 2*symbol:
        return get_available_main_diagonals(board)[0]

    if sum([board[i, BOARD_COLS - i - 1] for i in range(BOARD_COLS)]) == 2*symbol:
        return get_available_off_main_diagonals(board)[0]

    return None, None


class Player:
    """Player class"""

    def __init__(self, name, human=False):
        """init method"""

        self.name = name
        self.states = []  # states is a list of coordinate tuples (e.g. [(0,0), (0,2), ...]
        self.human = human

    def choose_action(self, current_board, symbol):
        """Choose action for the player based on the available positions (list) on the current_board (np.array)
           symbol is either 1 for player 1 or -1 for player 2
           return which action(tuple) should be taken"""

        # Rules for perfect play: https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy

        # Rule 1: If you have two in a row, place the third to win
        pos = check_two_in_a_row(current_board, symbol)

        # check if rule 1 applies
        if pos[0] is not None:
            return pos

        # Rule 2: If the opponent has two in a row, block the third to prevent from winning
        pos = check_two_in_a_row(current_board, -symbol)
        if pos[0] is not None:
            return pos

        # Rule 3 & 4: If you have two in opposing corners cause a fork so that you have two lines of winning
        # If the opponent can fork, prevent it

        # first, main diagonal
        # check if the main diagonal corners are the same
        if current_board[(0, 0)] == current_board[(2, 2)] != 0:

            # check if the off-diagonal corners are free -> if yes, place there
            if current_board[(0, 2)] == 0:
                return 0, 2
            elif current_board[(2, 0)] == 0:
                return 2, 0

        # second, off-diagonal
        if current_board[(0, 2)] == current_board[(2, 0)] != 0:
            if current_board[(0, 0)] == 0:
                return 0, 0
            elif current_board[(2, 2)] == 0:
                return 2, 2

        # Rule 5: Place in the center if it is free, but not on the first move
        if current_board[(1, 1)] == 0:
            if not np.any(current_board):  # any returns False if all elements are 0
                return tuple(np.random.choice([0, 2], size=2))
            else:
                return 1, 1

        # Rule 6: If the opponent is in a corner, play the opposite corner if possible
        for corner in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if current_board[corner] == -symbol:
                # check if the opposite corner is free, to calculate the opposite corner, do 0 -> 2, if 2 -> 0
                # this can be achieved by adding 2 and then modulo 4
                opposite_corner = (corner[0] + 2) % 4, (corner[1] + 2) % 4
                if current_board[opposite_corner] == 0:
                    return (corner[0] + 2) % 4, (corner[1] + 2) % 4

        # Rule 7: If there is an empty corner, place there
        for corner in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if current_board[corner] == 0:
                return corner

        # Rule 8: If there is an side ( = middle of top/bottom row or left/right col), place there
        # top & bottom row
        for i in [0, 2]:
            if current_board[(i, 1)] == 0:
                return i, 1
        # left & right col
        for j in [0, 2]:
            if current_board[(1, j)] == 0:
                return 1, j

        return None, None
