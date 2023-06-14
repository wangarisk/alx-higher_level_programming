#!/usr/bin/python3

def add_integer(a, b=98):

    """
    Adds two integers a and b.

    Args:
        a and b(int): Integers to be added.
        If they are floats, they are casted into integers first.

    Returns: 
        int: The sum of a and b.

    Raises: 
        TypeError: If a and b are floats.

    """
    if not isinstance(a, (int,float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int,float)):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)

    return(a + b)
