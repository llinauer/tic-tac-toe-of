#!/usr/bin/env python
"""
tic_tac_toe.py
Author: Lukas Linauer

Main module, parses command line arguments and sets up game

"""

import argparse
from game import Game


def main():
    """Main function"""

    # parse arguments
    parser = argparse.ArgumentParser(description='Play against an old-fashioned tic-tac-toe AI agent')
    parser.add_argument('-s', '--side', help='Choose side to play (X or O)', required=True,
                        type=str)

    args = parser.parse_args()
    if args.side not in ['x', 'X', 'o', 'O']:
        print('Please choose x or o')
        return

    side = args.side.upper()

    # initialize new game
    tic_tac_toe_game = Game(human_side=side)
    tic_tac_toe_game.play()


if __name__ == '__main__':
    main()
