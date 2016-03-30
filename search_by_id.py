"""Take in a command line argument in the form:
python search_by_id.py <db_filename>.sqlite <userID>
Print all cars associated with that user ID.
"""
import sqlite3
import sys
import user_id
import database

def unpack_user_input(user_input):
    """Take in a list of user input which contains a database filename
    and a user ID. Extract, validate, and return them as a tuple.
    """
    assert len(user_input) < 3, "Too many arguments given."
    assert len(user_input) > 1, "Too few arguments given."

    db_filename = user_input[0]
    assert database.is_valid_name(db_filename), "Invalid database filename."

    user_id_num = user_input[1]
    assert user_id.is_valid(user_id_num), "Invalid user ID."

    return (db_filename, user_id_num)

def search_by_id(user_id_num, db_cursor):
    """Take in a user ID as a string and a database cursor object. If
    the user ID exists in the database, return a list of each car
    associated with that user ID. Otherwise, return None.
    """
    assert user_id.is_valid(user_id_num), "Invalid user ID."
    select_statement = """SELECT car
                       FROM cars
                       WHERE userID =?"""
    users_cars = database.query(select_statement, user_id_num, db_cursor)
    return [car[0] for car in users_cars] if users_cars else None

if __name__ == "__main__":
    # Get command line arguments.
    RAW_USER_INPUT = sys.argv[1:]
    USER_INPUT = [ITEM.lower() for ITEM in RAW_USER_INPUT]

    # Extract the database filename and the user ID.
    DB_FILENAME, USER_ID = unpack_user_input(USER_INPUT)

    # Open and connect to a valid sqlite database.
    DATABASE = sqlite3.connect(DB_FILENAME)
    CURSOR = DATABASE.cursor()

    # Find and print the all cars associated with the given user ID.
    CARS = search_by_id(USER_ID, CURSOR)
    if CARS:
        for CAR in CARS:
            print CAR
    else:
        print "No cars were found for %s." % USER_ID

    # Close database.
    DATABASE.close()
