"""Extract and validate a list of cars."""
import re
from parse import parse

def are_valid(user_cars):
    """Take in a list of cars. Return True if every car in the list is
    valid. Otherwise, return False.
    """
    for car in user_cars:
        if not re.search(r"[\w.-]+", car):
            return False
    return True

def get_from_label(cars_str):
    """Take in a string in the format:
    'c: <car>, <car>, ...'
    Convert the result found after parsing into a list and return it.
    If there are no cars, return None.
    """
    user_cars = parse(r"(c: )(?P<cars>[\w.-]+(, [\w.-]+)*)",
                 "cars",
                 cars_str,
                )
    return user_cars.split(', ') if user_cars else None
