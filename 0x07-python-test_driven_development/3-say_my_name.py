#!/usr/bin/python3

""" Defines a function that prints the first and last name"""

def say_my_name(first_name, last_name=""):
    
    """
    The first and last names must be strings otherwise raise TypeError

    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))

