"""Open a text file, read in the content of the file, divide the
content into smaller chunks, and return the chunks.
"""
def chunk_file_contents(filename, chunk_size=1):
    """Take in a string 'filename' and an integer 'chunk_size'.
    Divide the file up into chunks that each contain the number of
    lines of data specified by the 'chunk_size'. For example, a
    chunk_size of 3 would yield a number of packages each containing 3
    lines of data from the text file.
    """
    content = read_file(filename)
    assert content, "There is nothing in the file: %s" % filename
    return chunk(content, chunk_size)

def read_file(file_name):
    """Read in all of the data from a text file and return it."""
    with open(file_name, 'r') as some_file:
        data = some_file.read()
    return data

def chunk(file_content, chunk_size):
    """Take in a large string of data called 'file_content' and an
    integer called 'chunk_size'. Divide the data into chunks which
    contain 'chunk_size' number of lines of data each and compile the
    chunks into a list. Return the list.
    """
    file_lines = file_content.splitlines()
    assert file_lines, "There is nothing in the file!"
    assert isinstance(chunk_size, int), "An integer must be given to determine the chunk size."
    assert 0 < chunk_size <= len(file_lines), "Inappropriate integer for the chunk size."
    assert len(file_lines) % chunk_size == 0, "Data is incomplete."
    return [file_lines[pos:pos + chunk_size] for pos in range(0, len(file_lines), chunk_size)]
