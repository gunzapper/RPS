#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Rock - Paper - Scissor game.

Usage:
  RPS.py P
  RPS.py S
  RPS.py R
  RPS.py -h | --help
  RPS.py -t | --test
  RPS.py --version

Options:
  -h --help     show this help message and exit.
  -t --test     execute tests.
  --version     show the version.
"""

from docopt import docopt

GAME_TABLE = {
    'R': 0,
    'P': 1,
    'S': 2
}


def who_wins(hand1, hand2):
    """
    >>> who_wins('R', 'S')
    1
    >>> who_wins('P', 'R')
    1
    >>> who_wins('S', 'P')
    1
    >>> who_wins('R', 'P')
    2
    >>> who_wins('S', 'R')
    2
    >>> who_wins('P', 'S')
    2
    >>> who_wins('R', 'R')
    0
    >>> who_wins('P', 'P')
    0
    >>> who_wins('S', 'S')
    0
    >>> who_wins('R', '?')
    Traceback (most recent call last):
        ...
    ValueError: only 'R', 'P' and 'S' are allowed input
    """
    try:
        return (GAME_TABLE[hand1] - GAME_TABLE[hand2]) % 3
    except KeyError:
        raise ValueError("only 'R', 'P' and 'S' are allowed input")


def main():
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    arguments = docopt(__doc__, version='Rock Paper Scissor 0.0.1')
    print(arguments)
    main()
