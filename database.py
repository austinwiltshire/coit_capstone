"""Validate the name of and make queries on an SQLite database."""
import re

def is_valid_name(filename):
    """Take in the name of a database as a string. Return True if it is
    a valid SQLite filename. Otherwise, return False.
    """
    if re.search(r"\b[\w.-]+.sqlite\b", filename):
        return True
    return False

def query(select_statement, search_term, db_cursor):
    """Take in an SQL select statement, a search term, and a database
    cursor. Execute the query on the database and return the results as
    a list.
    """
    db_cursor.execute(select_statement, (search_term,))
    data = db_cursor.fetchall()
    return data
