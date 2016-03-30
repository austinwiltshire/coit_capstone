"""Extract and validate a given name and a family name."""
import re
from parse import parse

def is_valid(name):
    """Take in a string containing a name. Return True if it is valid,
    Otherwise, return False.
    """
    return True if re.search("[a-zA-Z]+", name) else False

def get_given_name_from_label(given_name_str):
    """Take in a string in the format:
    'f: <given_name>'
    Return the results found after parsing.
    """
    given_name = parse("(f: )(?P<given_name>[a-zA-Z]+)",
                       "given_name",
                       given_name_str,
                      )
    return given_name

def get_family_name_from_label(family_name_str):
    """Take in a string in the format:
    'l: <family_name>'
    Return the results found after parsing.
    """
    family_name = parse("(l: )(?P<family_name>[a-zA-Z]+)",
                        "family_name",
                        family_name_str,
                       )
    return family_name

def assemble_full_name(user_name_tuple):
    """Take in a tuple containing two strings: a given name and a
    family name. Validate the names and return them as a single string
    in the format:
    <given_name> <family_name>
    """
    assert len(user_name_tuple) == 2

    given_name = user_name_tuple[0]
    assert is_valid(given_name), "Invalid first name."

    family_name = user_name_tuple[1]
    assert is_valid(family_name), "Invalid last name."

    return given_name + " " + family_name
