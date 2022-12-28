"""
player.py
Author: Lukas Linauer

Player module, used for making computer moves.
Chooses its move based on a simple set of rules.

"""

import numpy as np


class Player:
    """Player class"""

    def __init__(self, name, epsilon=0.4, vs_human=False):
        """init method"""

        self.name = name
        self.states = []  # states is a list of coordinate tuples (e.g. [(0,0), (0,2), ...]
        self.states_values = {}

        # RL parameters
        self.learning_rate = 0.3

        # when playing against a human, deactivate epsilon by setting it to -1
        if vs_human:
            self.epsilon = -1
        else:
            self.epsilon = epsilon
        self.decay_gamma = 0.9


    def choose_action(self, positions, current_board, symbol):
        """Choose action for the player based on the available positions (list),
           the current_board (np.array)
           symbol is either 1 for player 1 or -1 for player 2
           return which action(tuple) should be taken"""

        # generate random number between (0,1), if number <= epsilon => explore
        if np.random.uniform(0, 1) <= self.epsilon:
            idx = np.random.choice(len(positions))
            action = positions[idx]

        # choose action that leads to the maximum value
        else:

            max_value = -999

            # loop over all available positions
            for position in positions:
                next_board = current_board.copy()
                next_board[position] = symbol
                next_board_hash = get_hash(next_board)

                # check if the next_board_state already has a value assigned
                value = self.states_values.get(next_board_hash)
                if not value:
                    value = 0

                if value >= max_value:
                    max_value = value
                    action = position

        return action
