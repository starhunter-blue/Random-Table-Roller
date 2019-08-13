import re
from exceptions import InvalidEntryNumberingException

ENTRY_NUMBERING_VALID_REGEX = re.compile(r"(\d+(-\d+)*:)")
ENTRY_SINGLE_NUMBER_REGEX = re.compile(r"(\d+:)")
ENTRY_RANGE_REGEX = re.compile(r"\d+-\d+:")

def create_table(name, entries):
    results = []

    for entry in entries:
        if not is_entry_numbering_valid(entry):
            raise InvalidEntryNumberingException(name + " : " + entry)

        single_entry_nr = re.match(ENTRY_SINGLE_NUMBER_REGEX, entry)
        range_entry_nr = re.match(ENTRY_RANGE_REGEX, entry)
        if single_entry_nr is not None:
            print(single_entry_nr.group())
        
        elif range_entry_nr is not None:
            print("Range: " + range_entry_nr.group())
    


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

entries = ["1: Test", "2: Test", "3-10: Test"]
create_table("Bla", entries)