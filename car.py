"""Extract and validate car names."""
import re
from parse import parse

def is_valid(car_name):
    """Take in a string containing a car name. Return True if it is
    valid name. Otherwise, return False.
    """
    return True if re.search(r"[\w.-]+", car_name) else False

def are_valid(car_names):
    """Take in a list of car names. Return True if every car in the list is
    valid. Otherwise, return False.
    """
    return True if all([is_valid(car_name) for car_name in car_names]) else False

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
