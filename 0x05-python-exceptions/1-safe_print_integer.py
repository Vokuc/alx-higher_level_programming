#!/bin/usr/python3

def safe_print_integer(value):
    """print an integer with format.

    Args:
        value (int): the integer to print.

    Returns:
        If a TypeError or ValueError occurs - False
        Otherwise True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
