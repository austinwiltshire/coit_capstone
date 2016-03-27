"""Open a text file, read in the data from the file, divide the data up into smaller
pieces, and return the pieces.
"""
def get_data(filename, package_size=1):
    """Take in a string 'filename' and an integer 'package_size'.
    Divide the file up into packages that each contain the number of
    lines of data specified by the 'package_size'. For example, a
    package_size of 3 would yield a various amount of packages each
	containing 3 lines of data from the read text file.
    """
    data = read_file(filename)
    assert data, "There is no data in file: %s" % filename
    return package_file_data(data, package_size)

def read_file(file_name):
    """Read in all of the data from a text file and return it."""
    with open(file_name, 'r') as some_file:
        data = some_file.read()
    return data

def package_file_data(file_data, package_size):
    """Take in a large string of data and an integer called
    'package_size'. Divide the data into a list of packages of data
    which contain 'package_size' lines of data each. Return the list.
    """
    data_lines = file_data.splitlines()
    assert data_lines, "There is no data!"
    assert isinstance(package_size, int), "An integer must be provided for the package size."
    assert 0 < package_size <= len(data_lines), "Inappropriate integer for the package size."
    assert len(data_lines) % package_size == 0, "Data is incomplete."
    return [data_lines[pos:pos + package_size] for pos in range(0, len(data_lines), package_size)]
