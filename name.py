"""Extract and validate a given name and a family name."""
import re
from parse import parse

def is_valid(name):
    """Take in a string containing a name. Return True if it is valid,
    Otherwise, return False.
    """
    if re.search("[a-zA-Z]+", name):
        return True
    return False

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
