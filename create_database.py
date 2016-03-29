"""Read in data from a text file. Manipulate the data and insert it
into an SQLite database with a 'users table' that has columns:
userID, given_name, family_name
and a 'cars table' that has columns:
car, owner
Return a completion message upon completion.
"""
import sqlite3
import name
import car
import read_file
import user_id

def unpack_data(data_package):
    """Take in a list of 3 strings which contain data in the following
    formata:
    ['f: <given_name>',
     'l: <family_name>',
     'c: <car>, <car>, <car>,...']
    If the data package contains valid examples of all three elements,
    extract the elements from their respective labels and return a
    tuple of the isolated elements. Otherwise, return None.
    """
    assert len(data_package) == 3, "Data packages consist of 3 strings of information."
    given_name = name.get_given_name_from_label(data_package[0].lower())
    family_name = name.get_family_name_from_label(data_package[1].lower())
    user_cars = car.get_from_label(data_package[2])

    if given_name and family_name and user_cars:
        return (given_name,
                family_name,
                user_cars,)
    else:
        return None

def prep_data(data_objects):
    """Take in a list of data_objects in the format:
    [('<given_name>', '<family_name>', ['<car>']),
     ('<given_name>', '<family_name>', ['<car>', '<car>']),
	 ('<given_name>', '<family_name>', ['<car>'])...]
    Use the data in each data_object to create a unique userID and two
    lists of tuples.
    Prepare the first list for the rows of data in the 'users table'.
    Prepare the second list for the rows of data in the 'cars table'.
    Return the lists.
    """
    user_data_rows = []
    car_data_rows = []

    for data_object in data_objects:
        if data_object:
            assert len(data_object) == 3, "Data object needs 3 elements."

			# Prepare the data rows for the 'users table'.
            given_name = data_object[0]
            assert name.is_valid(given_name)
            family_name = data_object[1]
            assert name.is_valid(family_name)
            id_number = user_id.create(given_name, family_name)
            assert user_id.is_valid(id_number)
            user_data_rows.append((id_number, given_name, family_name))

            # Prepare the data rows for the 'cars table'.
            cars = data_object[2]
            assert car.are_valid(cars)
            for each_car in cars:
                car_data_rows.append((each_car, id_number))

    return user_data_rows, car_data_rows

def create_users_table(db_cursor, user_data_rows):
    """Create a table of users with columns for userID, given_name,
    and family_name. Insert the user_data_rows into the table.
    """
    # Create 'users table' in the given database.
    db_cursor.execute("""
        CREATE TABLE users(userID TEXT PRIMARY KEY,
                           given_name TEXT,
                           family_name TEXT)
    """)

    # Insert user data rows into the 'users table'.
    for row in user_data_rows:
        if row:
            assert len(row) == 3, "Wrong amount of information in the row of data."

            db_cursor.execute("""INSERT INTO users(userID, given_name, family_name)
                              VALUES(?,?,?)""", row)

def create_cars_table(db_cursor, car_data_rows):
    """Create a table of cars with columns for car and owner. Insert
    the car_data_rows into the table.
    """
    # Create 'cars table' in the given database.
    db_cursor.execute("""
        CREATE TABLE cars(car TEXT,
                          owner TEXT)
    """)

    # Insert car data rows into the 'cars table'.
    for row in car_data_rows:
        if row:
            assert len(row) == 2, "Wrong amount of information in the row of data."

            db_cursor.execute("""INSERT INTO cars(car, owner)
                              VALUES(?,?)""", row)

if __name__ == "__main__":
    # Create users' cars database file and connect to it.
    DB_FILENAME = 'users_cars.sqlite' # Insert desired database filename here.
    DATABASE = sqlite3.connect(DB_FILENAME)
    DB_CURSOR = DATABASE.cursor()

    # Extract data from text file.
    FILENAME = 'cars.txt' # Insert data input filename here.
    DATA_PACKAGES = read_file.get_data(FILENAME, package_size=3)
    DATA_OBJECTS = [unpack_data(DATA_PACKAGE) for DATA_PACKAGE in DATA_PACKAGES]

    # Prepare the data objects for insertion into tables in the database.
    USER_DATA_ROWS, CAR_DATA_ROWS = prep_data(DATA_OBJECTS)

    # Create data tables in the users' cars database.
    create_users_table(DB_CURSOR, USER_DATA_ROWS)
    create_cars_table(DB_CURSOR, CAR_DATA_ROWS)

    # Make user IDs text file for future reference.
    ID_OUTPUT_FILENAME = 'userIDs.txt' # Insert desired IDs list text filename here.
    user_id.write_to_file(DB_CURSOR, ID_OUTPUT_FILENAME)

    # Save and close the database.
    DATABASE.commit()
    DATABASE.close()

    print "Database complete."
    print "Database: %s" % DB_FILENAME
    print "User IDs: %s" % ID_OUTPUT_FILENAME
