import re
from exceptions import InvalidEntryNumberingException, DuplicateEntryException

ENTRY_NUMBERING_VALID_REGEX = re.compile(r"(\d+(-\d+)*:)")
ENTRY_SINGLE_NUMBER_REGEX = re.compile(r"^(\d+):(.*)")
ENTRY_RANGE_REGEX = re.compile(r"\d+-\d+:")

def create_table(name, entries):
    results = {}

    def add_single_entry(single_entry):
        entry_nr = int(single_entry.group(1))
        entry_value = single_entry.group(2)
        check_if_duplicate_entry(entry_nr)
        results[entry_nr] = entry_value

    def check_if_duplicate_entry(entry_nr):
        if entry_nr in results:
            raise DuplicateEntryException

    for entry in entries:
        if not is_entry_numbering_valid(entry):
            raise InvalidEntryNumberingException(name + " : " + entry)

        single_entry = re.search(ENTRY_SINGLE_NUMBER_REGEX, entry)
        range_entry_nr = re.match(ENTRY_RANGE_REGEX, entry)
        if single_entry is not None:
            try:
                add_single_entry(single_entry)
            except DuplicateEntryException as e:
                raise DuplicateEntryException("Numbers used by this entry are already in use: " + entry).with_traceback(e.__traceback__)
        
        elif range_entry_nr is not None:
            pass
            #print("Range: " + range_entry_nr.group())

        print(results)
    


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

entries = ["1: 1-4:", "2: Test", "3-10: Test"]
create_table("Bla", entries)