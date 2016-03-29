"""Test the functions which belong to the create_database module."""
import sqlite3
import create_database
import read_file
import user_id

def test_unpack_data():
    """Assert unpack_data returns the correct output when given various
    lists of 3 inputs.
    """
    # Expected input.
    assert create_database.unpack_data(['f: coit',
                                        'l: scharringhausen',
                                        'c: focus, elantra']) == ('coit',
                                                                  'scharringhausen',
                                                                  ['focus', 'elantra'])
    # No given name.
    assert not create_database.unpack_data(['f: ', 'l: scharringhausen', 'c: focus, elantra'])
    # Invalid given name.
    assert not create_database.unpack_data(['f: 12345', 'l: scharringhausen', 'c: focus, elantra'])
    # No family name.
    assert not create_database.unpack_data(['f: coit', 'l: ', 'c: focus, elantra'])
    # Invalid family name.
    assert not create_database.unpack_data(['f: coit', 'l: 12345', 'c: focus, elantra'])
    # No car.
    assert not create_database.unpack_data(['f: coit', 'l: scharringhausen', 'c: '])
    # Invalid car.
    assert not create_database.unpack_data(['f: coit', 'l: scharringhausen', 'c: !@#$%'])

def test_prep_data():
    """Assert correct return values and order for a sample list input
    to prep_data().
    """
    test_input = [('cora', 'namkung', ['sonata']),
                  ('john', 'graham', ['tiburon', 'civic']),
                  ('ashley', 'gay', ['prius'])]
    user_data_output, car_data_output = create_database.prep_data(test_input)

    # Check correct data output amount.
    assert len(user_data_output) == 3
    assert len(car_data_output) == 4

    # Check user IDs/owner output.
    for i in range(0, len(user_data_output)):
        assert user_id.is_valid(user_data_output[i][0])
        assert user_id.is_valid(car_data_output[i][1])

    # Check given names output.
    assert user_data_output[0][1] == 'cora'
    assert user_data_output[1][1] == 'john'
    assert user_data_output[2][1] == 'ashley'

    # Check family names output.
    assert user_data_output[0][2] == 'namkung'
    assert user_data_output[1][2] == 'graham'
    assert user_data_output[2][2] == 'gay'

    # Check cars output.
    assert car_data_output[0][0] == 'sonata'
    assert car_data_output[1][0] == 'tiburon'
    assert car_data_output[2][0] == 'civic'
    assert car_data_output[3][0] == 'prius'

def test_create_tables():
    """Assert the correct contents of the users and cars table."""
    # Create test database.
    test_database = sqlite3.connect('test_database.sqlite')
    cursor = test_database.cursor()
    data_packages = read_file.get_data('test_data.txt', package_size=3)
    data_objects = [create_database.unpack_data(data_package) for data_package in data_packages]
    user_data_rows, car_data_rows = create_database.prep_data(data_objects)

    # Create test users and cars tables.
    create_database.create_users_table(cursor, user_data_rows)
    create_database.create_cars_table(cursor, car_data_rows)

    # Check user IDs from the users table.
    select_statement = """SELECT userID
                       FROM users"""
    cursor.execute(select_statement)
    id_numbers = cursor.fetchall()
    for i in range(0, len(id_numbers)):
        assert user_id.is_valid(id_numbers[i][0])

    # Check a sample first name and last name from the users table.
    select_statement = """SELECT given_name, family_name
                       FROM users"""
    cursor.execute(select_statement)
    name = cursor.fetchone()
    assert name[0] == 'bob'
    assert name[1] == 'marley'

    # Check user IDs from the cars table.
    select_statement = """SELECT owner
                       FROM cars"""
    cursor.execute(select_statement)
    id_numbers = cursor.fetchall()
    for i in range(0, len(id_numbers)):
        assert user_id.is_valid(id_numbers[i][0])

    # Check a sample car from the cars table.
    select_statement = """SELECT car
                       FROM cars"""
    cursor.execute(select_statement)
    name = cursor.fetchone()
    assert name[0] == 'f150'

    test_database.close()
