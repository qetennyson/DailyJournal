"""this is the journal module"""

import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with file data.
    """
    # todo: populate from file if it exists
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """ Saves the journal data (fout = file output stream """
    # todo: this code is what you would require without import os (annotate)
    # base_dir = "~/myworkingfolder"
    # rel_dir = "data/temp.txt"
    #
    # full_file = base_dir + '/' + rel_dir

    """ This pattern for os.path provides the explicit, 
    full path for the file."""

    filename = get_full_pathname(name)
    print("..... saving to: {}".format(filename))

    # replaces open and close with a safer method for clean-up
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
