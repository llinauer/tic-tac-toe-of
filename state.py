"""
state.py
Author: Lukas Linauer

Keeps track of board states

"""

import numpy as np

# 3x3 board
BOARD_ROWS = 3
BOARD_COLS = 3


def get_available_positions(board):
    """Return positions in board(np.ndarray) with no X or O in them"""

    positions = []
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i, j] == 0:
                positions.append((i, j))
    return positions


class State:
    """State class"""

    def __init__(self):
        """init method"""

        self.board = np.zeros((BOARD_ROWS, BOARD_COLS))
        self.is_end = False

        # X (=1) goes first
        self.player_symbol = 1

    def update_state(self, position):
        """Update the board with position (tuple(i,j))"""

        self.board[position] = self.player_symbol
        # switch to other player
        self.player_symbol = -1 if self.player_symbol == 1 else 1

    def check_win(self):
        """
        Checks the board if a a player has won
        Return 1 if player 1 won, -1 if player 2 won, 2 in case of draw
        """

        # check rows
        for i in range(BOARD_ROWS):
            if sum(self.board[i, :]) == 3:
                self.is_end = True
                return 1
            elif sum(self.board[i, :]) == -3:
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

        if diag_sum1 == 3 or diag_sum2 == 3:
            self.is_end = True
            return 1
        if diag_sum1 == -3 or diag_sum2 == -3:
            self.is_end = True
            return -1

        # check for draw
        if len(self.get_available_positions()) == 0:
            self.is_end = True
            return 2

        return None
