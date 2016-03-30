"""Take in a command line argument in the form:
python search_by_car.py <db_filename>.sqlite <car_name>
Print the full names of all the users who own that type of car.
"""
import sqlite3
import sys
import name
import car
import database

def unpack_user_input(user_input):
    """Take in a list of user input which contains a database filename
    and a car name. Extract, validate, and return them as a tuple.
    """
    assert len(user_input) < 3, "Too many arguments given."
    assert len(user_input) > 1, "Too few arguments given."

    db_filename = user_input[0]
    assert database.is_valid_name(db_filename), "Invalid database filename."

    car_name = user_input[1]
    assert car.is_valid(car_name), "Invalid car name."

    return (db_filename, car_name)

def search_by_car(car_name, db_cursor):
    """Take in a car name as a string and a database cursor object. If
    the car exists in the database, return a list of each user's full
    name who owns that type of car. Otherwise, return None.
    """
    assert car.is_valid(car_name), "Invalid car name."
    select_statement = """SELECT given_name, family_name
                       FROM users, cars
                       WHERE users.userID = cars.userID
                           AND car =?
                       GROUP BY given_name"""
    users = database.query(select_statement, car_name.lower(), db_cursor)
    return [name.assemble_full_name(user) for user in users] if users else None

if __name__ == "__main__":
    # Get command line arguments.
    RAW_USER_INPUT = sys.argv[1:]
    USER_INPUT = [ITEM.lower() for ITEM in RAW_USER_INPUT]

    # Extract the database filename and the car name.
    DB_FILENAME, CAR_NAME = unpack_user_input(USER_INPUT)

    # Open and connect to a valid sqlite database.
    DATABASE = sqlite3.connect(DB_FILENAME)
    CURSOR = DATABASE.cursor()

    # Find and print the full names of each user who owns that type of car.
    USERS = search_by_car(CAR_NAME, CURSOR)
    if USERS:
        for USER in USERS:
            print USER
    else:
        print "No users in the database own a %s." % CAR_NAME

    # Close database.
    DATABASE.close()
