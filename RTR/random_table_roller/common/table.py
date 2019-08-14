import re
from exceptions import InvalidEntryNumberingException, DuplicateEntryException, EntryMissingException, UnclearTableNameException

ENTRY_NUMBERING_VALID_REGEX = re.compile(r"(\d+(-\d+)*:)")
ENTRY_SINGLE_NUMBER_REGEX = re.compile(r"^(\d+):(.*)")
ENTRY_RANGE_REGEX = re.compile(r"^(\d+-\d+):(.*)")

def create_table(name, entries):
    results = {}
    die_size = 0

    def add_entry(entry_nr, entry_value):
        check_if_duplicate_entry(entry_nr)
        results[entry_nr] = entry_value

    def add_range_entry(range_entry):
        entry_range_str = range_entry.group(1).split("-")
        entry_range = range(int(entry_range_str[0]), int(entry_range_str[1]) + 1)
        entry_value = range_entry.group(2)
        for i in entry_range:
            add_entry(i, entry_value)

    def check_if_duplicate_entry(entry_nr):
        if entry_nr in results:
            raise DuplicateEntryException
    
    def check_if_all_entries_present():
        for i in range(1, die_size + 1):
            if i not in results:
                raise EntryMissingException(str(i) + " is missing from table as die result")

    if name[:2] != "**" and name[0] != "*":
        raise UnclearTableNameException("Table name: " + name + 
                                        "\n Table name must begin with * for a Table or ** for a Subtable")

    for entry in entries:
        if not is_entry_numbering_valid(entry):
            raise InvalidEntryNumberingException(name + " : " + entry)

        single_entry = re.search(ENTRY_SINGLE_NUMBER_REGEX, entry)
        range_entry = re.search(ENTRY_RANGE_REGEX, entry)
        try:
            if single_entry is not None:
                    entry_nr = int(single_entry.group(1))
                    entry_value = single_entry.group(2)
                    add_entry(entry_nr, entry_value)
            elif range_entry is not None:
                add_range_entry(range_entry)
        except DuplicateEntryException as e:
            raise DuplicateEntryException("Numbers used by this entry are already in use: " + entry).with_traceback(e.__traceback__)
    
        
    die_size = max(results.keys())

    check_if_all_entries_present()

    


def is_entry_numbering_valid(entry):
    return re.match(ENTRY_NUMBERING_VALID_REGEX, entry) != None

class Table():
    
    def __init__(self, name):
        self.name = name

class SimpleTable(Table):
    
    def __init__(self, name):
        super().__init__(self, name)

class ComplexTable(Table):
    def __init__(self, name):
        super().__init__(self, name)

entries = ["1: 1-4:", "2: Test", "3-6: Dom"]
create_table("Bla", entries)