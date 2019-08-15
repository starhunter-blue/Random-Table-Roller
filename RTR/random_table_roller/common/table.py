import re
from exceptions import *

class Table:
    ENTRY_NUMBERING_VALID_REGEX = re.compile(r"(\d+(-\d+)*:)")

    @staticmethod
    def is_entry_numbering_valid(entry):
        return re.match(Table.ENTRY_NUMBERING_VALID_REGEX, entry) != None

    def __init__(self, raw_table):
        self.name = raw_table[0]
        self.raw_content = raw_table[1:]
        self.content = {}

        #Check if name follows naming convention
        unclear_name_exception = UnclearTableNameException(self.name 
                                                            + " does not follow table naming conventions. \n"
                                                            + "Tables must either start/end with </> for <Tables> \n"
                                                            + "or start/end with <</>> for <<Subtables>>."
                                                          )
        if self.name[:2] == "<<":
            if self.name[-2:] != ">>":
                raise unclear_name_exception
        elif self.name[0] == "<":
            if self.name[-1:] != ">" or self.name[-2:] == ">>":
                raise unclear_name_exception
        else:
            raise unclear_name_exception

    def parse_raw_content(self, table_registry):
        if len(self.raw_content) < 1:
            raise EmptyTableException(self.name + " contains no entries")

        for entry in self.raw_content:
            if not Table.is_entry_numbering_valid(entry):
                raise InvalidEntryNumberingException("Table " + self.name + " contains incorrectly numbered entry " 
                                                        + entry)       




test1 = []
test2 = []
test3 = []
test4 = []
test5 = []
test1.append("<Test1>")
test1.append("1: A")
test1.append("2-3: B")
test1.append("4: C")
table = Table(test1)
table_registry = {}
table_registry[table.name] = table 
table.parse_raw_content(table_registry)
