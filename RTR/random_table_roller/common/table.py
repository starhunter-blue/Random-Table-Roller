import re
from random_table_roller.common.exceptions import *

class Table:
    ENTRY_NUMBERING_VALID_REGEX = re.compile(r"(\d+(-\d+)*:)")
    ENTRY_SINGLE_NUMBER_REGEX = re.compile(r"^(\d+):(.*)")
    ENTRY_RANGE_REGEX = re.compile(r"^(\d+-\d+):(.*)")

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

            single_entry = re.search(Table.ENTRY_SINGLE_NUMBER_REGEX, entry)
            range_entry = re.search(Table.ENTRY_RANGE_REGEX, entry)
            
            try:
                if single_entry is not None:
                    entry_nr = int(single_entry.group(1))
                    entry_value = single_entry.group(2)
                    print(str(entry_nr) + " " + entry_value)
            except RandomTableRollerException:
                pass           


class Entry:
    @staticmethod
    def decompose_into_components(entry_value):
        split_components = entry_value.split("-->", 1)

        first_component_text = split_components[0]

        if len(split_components) < 2:
            return
        second_component_text = split_components[0].strip()

        if second_component_text[0] == "[" and second_component_text[-1:] == "]":
            pass
        else: 
            pass

        #if len(split_components) == 1
        #entry return = split_components[0]

        #if len(split_components) == 2
        #entry return = split_components[0] + parsed/rolled split_component[1]

        #else fatal error


    def __init__(self, entry_value, table_registry):
        pass