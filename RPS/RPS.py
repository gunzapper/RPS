#!/usr/bin/env python3
# -*- coding: utf-8 -*-


GAME_TABLE = {
    'R': 0,
    'P': 1,
    'S': 2
}


def who_wins(hand1, hand2):
    """
    >>> who_wins('R', 'S')
    1
    >>> who_wins('R', 'P')
    2
    >>> who_wins('R', 'R')
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
    main()
