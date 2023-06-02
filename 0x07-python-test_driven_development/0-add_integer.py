#!/usr/bin/python3

""" defines a function adding integers"""

def add_integer(a, b=98):

    """
    The function adds two integers a and b.
    If and a and b are floats,they are casted into integers first.
    It raises a TypeError if a or b are not integers.
    It returns the addition of the two integers.

    """
    if not isinstance(a, (int,float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int,float)):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)

    return(a + b)
