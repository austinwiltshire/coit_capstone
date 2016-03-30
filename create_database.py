"""Read in data from a text file. Manipulate the data and insert it
into an SQLite database with a 'users table' that has columns:
userID, given_name, family_name
and a 'cars table' that has columns:
car, owner
Return a completion message upon completion.
"""
import sqlite3
import User
import name
import car
import read_file
import user_id

def create_user(textfile_chunk):
    """Take in a list of 3 strings which contain data in the following
    formata:
    ['f: <given_name>',
     'l: <family_name>',
     'c: <car>, <car>, <car>,...']
    If the textfile chunk contains valid examples of all three elements,
    extract the elements from their respective labels and return a
    User object. Otherwise, return None.
    """
    assert len(textfile_chunk) == 3, "Data chunk should consist of 3 strings."
    given_name = name.get_given_name_from_label(textfile_chunk[0].lower())
    family_name = name.get_family_name_from_label(textfile_chunk[1].lower())
    user_cars = car.get_from_label(textfile_chunk[2])

    if given_name and family_name and user_cars:
        return User.User(given_name, family_name, user_cars)
    else:
        return None

def prep_users_table_content(users_list):
    """Take in a list of User objects. Return a list of tuples in the
    format:
    (<user_id>, <user_given_name>, <user_family_name>)
    """
    return [(user.get_user_id(),
             user.get_given_name(),
             user.get_family_name()) for user in users_list if user]

def prep_cars_table_content(users_list):
    """Take in a list of User objects. Return a list of tuples in the
    format:
    (<user_id>, <user_car>)
    """
    cars_table_rows = []
    for user in users_list:
        if user:
            users_cars = user.get_cars()
            for users_car in users_cars:
                cars_table_rows.append((user.get_user_id(), users_car))
    return cars_table_rows

def create_users_table(db_cursor, users_table_rows):
    """Create a table of users with columns for userID, given_name,
    and family_name. Insert the users_table_rows into the table.
    """
    # Create 'users table' in the given database.
    db_cursor.execute("""
        CREATE TABLE users(userID TEXT PRIMARY KEY,
                           given_name TEXT,
                           family_name TEXT)
    """)

    # Insert 'users table rows' into the 'users table'.
    for row in users_table_rows:
        if row:
            assert len(row) == 3, "Wrong amount of information in the table row."

            db_cursor.execute("""INSERT INTO users(userID, given_name, family_name)
                              VALUES(?,?,?)""", row)

def create_cars_table(db_cursor, cars_table_rows):
    """Create a table of cars with columns for car and owner. Insert
    the cars_table_rows into the table.
    """
    # Create 'cars table' in the given database.
    db_cursor.execute("""
        CREATE TABLE cars(userID TEXT,
                          car TEXT)
    """)

    # Insert 'cars table rows' into the 'cars table'.
    for row in cars_table_rows:
        if row:
            assert len(row) == 2, "Wrong amount of information in the table row."

            db_cursor.execute("""INSERT INTO cars(userID, car)
                              VALUES(?,?)""", row)

if __name__ == "__main__":
    # Create users' cars database file and connect to it.
    DB_FILENAME = 'users_cars.sqlite' # Insert desired database filename here.
    DATABASE = sqlite3.connect(DB_FILENAME)
    DB_CURSOR = DATABASE.cursor()

    # Extract data from text file.
    FILENAME = 'cars.txt' # Insert data input filename here.
    TEXTFILE_CHUNKS = read_file.chunk_file_contents(FILENAME, chunk_size=3)
    USERS = [create_user(TEXTFILE_CHUNK) for TEXTFILE_CHUNK in TEXTFILE_CHUNKS]

    # Prepare the Users for insertion into the tables of the database.
    USERS_TABLE_ROWS = prep_users_table_content(USERS)
    CARS_TABLE_ROWS = prep_cars_table_content(USERS)

    # Create the tables and insert the Users into the database.
    create_users_table(DB_CURSOR, USERS_TABLE_ROWS)
    create_cars_table(DB_CURSOR, CARS_TABLE_ROWS)

    # Make user IDs text file for future reference.
    ID_OUTPUT_FILENAME = 'userIDs.txt' # Insert desired IDs list text filename here.
    user_id.write_to_file(DB_CURSOR, ID_OUTPUT_FILENAME)

    # Save and close the database.
    DATABASE.commit()
    DATABASE.close()

    print "Database complete."
    print "Database: %s" % DB_FILENAME
    print "User IDs: %s" % ID_OUTPUT_FILENAME
