#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def who_wins(hand1, hand2):
    """
    >>> who_wins('R', 'S')
    1
    >>> who_wins('R', 'P')
    2
    >>> who_wins('R', 'R')
    3
    >>> who_wins('R', '?')
    Traceback (most recent call last):
        ...
    ValueError: only 'R', 'P' and 'S' are allowed input
    """

    pass

def main():
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
