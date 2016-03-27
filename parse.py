"""Use regular expressions to parse a piece of data from a string."""
import re

def parse(regex, group_name, string):
    """Take in a regular expression which utlizes grouping, the group
    name used in the given regular expression, and a string to be
    analyzed. Return a found match. Otherwise, return None.
    """
    parsed_data = re.search(regex, string)
    if parsed_data:
        return parsed_data.group(group_name)
    return None
