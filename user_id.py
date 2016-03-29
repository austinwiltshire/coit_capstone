"""Use a given name string, a family name string, and a random integer
between 100 and 999 to create a user_id.
"""
import random
import re
import name

def is_valid(user_id_str):
    """Take in a string containing a user ID. Return True if it is
    valid user ID. Otherwise, return False.
    """
    if re.search("[a-zA-Z]+[0-9][0-9][0-9]", user_id_str):
        return True
    return False

def create(given_name, family_name):
    """Take in two strings: a given_name and a family_name. Use the
    strings and a random integer between 100 and 999 to create a unique
    user_id. Example using John Smith:
    jsmith###
    """
    assert name.is_valid(given_name)
    id_head = given_name[0].lower()

    assert name.is_valid(family_name)
    id_body = family_name.lower()

    id_tail = random.randint(100, 999)

    return id_head + id_body + str(id_tail)

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
