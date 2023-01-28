#!/usr/bin/env python
"""
tic_tac_toe.py
Author: Lukas Linauer

Main module, parses command line arguments and sets up game

"""

import sys
import argparse
from game import Game


def main():
    """Main function"""


    # parse arguments
    parser = argparse.ArgumentParser(description='Train an Reinforcement Learning agent in Tic '
                                                 'Tac Toe and play against it')

    # initialize new game
    tic_tac_toe_game = Game(vs_human=True)
    tic_tac_toe_game.player_vs_computer()


if __name__ == '__main__':
    main()
