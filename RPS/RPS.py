#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Rock - Paper - Scissor game.

Usage:
  RPS.py <hand>
  RPS.py -i | --inter
  RPS.py -h | --help
  RPS.py -t | --test
  RPS.py --version

Options:
  -h --help     show this help message and exit.
  -t --test     execute tests.
  -i --inter    launch interactive mode
  --version     show the version.
"""

import random

from docopt import docopt

GAME_TABLE = {
    'R': 0,
    'P': 1,
    'S': 2
}

Nice_comments = {
    'R': "Rock breaks scissor",
    'S': "Scissor cuts paper",
    'P': "Paper lines rock"
}

results = [
    "Nobody won, nobody lose",
    "You won",
    "I beated you"
]


def who_wins(hand1, hand2):
    """
    Determine who wins at rock paper scissor game using Modular matematic

    In this function:
        * 'R' accounts for 'rock'
        * 'P' accounts for 'paper'
        * 'S' accounts for 'scissor'

    Args:
        hand1 (str): The hand of the first player
        hand2 (str): The hand of the second player

    Returns:
        int.  The return code::

          0 -- Pair
          1 -- first player won.
          2 -- second player won.

    Raises:
        ValueError

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


def interactive_session():

    random.seed()
    result = ''
    while True:
        bots_hand = random.choice('SPR')
        print("Play your hand")
        players_hand = yield result
        result = out_match(bots_hand, players_hand)


def out_match(players_hand, bots_hand):
    """ print a nice output result

    Args:
        players_hand (str): The hand of the player
        bots_hand (str): The end of this script

        >>> print(out_match('P', 'S'))
        You played P
        I played S
        I beated you
        Scissor cuts paper
        >>> print(out_match('P', 'R'))
        You played P
        I played R
        You won
        Paper lines rock
        >>> print(out_match('P', 'P'))
        You played P
        I played P
        Nobody won, nobody lose
        <BLANKLINE>
    """

    point = who_wins(players_hand, bots_hand)

    if point == 1:
        nice_end = Nice_comments[players_hand]
    elif point == 2:
        nice_end = Nice_comments[bots_hand]
    else:
        nice_end = ''

    return("You played {0}\nI played {1}\n{2}\n{3}".format(
        players_hand,
        bots_hand,
        results[point],
        nice_end
    ))


def main(args):

    if args['--test']:
        print('testing...')
        import doctest
        doctest.testmod()

    if args['<hand>']:
        random.seed()
        bots_hand = random.choice('SPR')
        out_match(args['<hand>'], bots_hand)

    if args['--inter']:
        # for the moment it does not work
        pass

if __name__ == "__main__":

    arguments = docopt(__doc__, version='Rock Paper Scissor 0.0.1')
    main(arguments)
