"""Use two strings, 'given_name' and 'family_name', to create a hash
value as the user_id.
"""
import re
import hashlib
import name

def is_valid(user_id_str):
    """Take in a string containing a user ID. Return True if it is
    valid. Otherwise, return False.
    """
    return True if re.search("[a-zA-Z0-9]{56}", user_id_str) else False

def create(given_name, family_name):
    """Take in two strings: a given_name and a family_name. Validate
    them and use them to create user ID as a hash value. Return the ID.
    """
    assert name.is_valid(given_name)
    assert name.is_valid(family_name)
    return hashlib.sha224(b""+given_name+" "+family_name).hexdigest()

def write_to_file(db_cursor, txt_filename):
    """Take in a database cursor object and a desired text filename.
    Find all the userIDs in the database and print them to a text file.
    """
    select_statement = """SELECT userID
                       FROM users"""
    db_cursor.execute(select_statement)
    user_ids = db_cursor.fetchall()
    user_ids_file = open(txt_filename, 'w')
    for i in range(0, len(user_ids)):
        user_ids_file.write(user_ids[i][0]+'\n')
    user_ids_file.close()
