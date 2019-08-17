import re
import random
from random_table_roller.common.exceptions import DuplicateEntryException,\
                                                  EmptyTableException,\
                                                  InvalidEntryNumberingException,\
                                                  MissingTableException,\
                                                  TableNotYetParsedException,\
                                                  UnclearSubEntryException,\
                                                  UnclearTableNameException

class Table:
    """Table class containing one or more entries and the capability to create a random result from itself.
    Must first be provided with the table as a raw string.
    Can only be parsed into a proper table once all tables are instantiated and the table_registry is provided."""
    ENTRY_NUMBERING_VALID_REGEX = re.compile(r"(\d+(-\d+)*:)")
    ENTRY_SINGLE_NUMBER_REGEX = re.compile(r"^(\d+):(.*)")
    ENTRY_RANGE_REGEX = re.compile(r"^(\d+-\d+):(.*)")

    @staticmethod
    def is_entry_numbering_valid(entry):
        """Checks if the provided string provides a correct entry numbering, ie. starts either with
        [int]: or [int]-[int]:"""
        return re.match(Table.ENTRY_NUMBERING_VALID_REGEX, entry) != None

    def __init__(self, raw_table):
        self.name = raw_table[0]
        self.raw_content = raw_table[1:]
        self.content = {}
        self.table_size = 0
        self.subtable = False

        #Check if name follows naming convention
        unclear_name_exception = UnclearTableNameException(self.name
                                                           + " does not follow table naming conventions."
                                                           +"\nTables must either start/end with </> for <Tables>" 
                                                           +"\n or start/end with <</>> for <<Subtables>>.")
        if self.name[:2] == "<<":
            if self.name[-2:] != ">>":
                raise unclear_name_exception
        elif self.name[0] == "<":
            if self.name[-1:] != ">" or self.name[-2:] == ">>":
                raise unclear_name_exception
        else:
            raise unclear_name_exception

        if self.name[:2] == "<<":
            self.subtable = True

    def parse_raw_content(self, table_registry):
        """Turns the raw string content of the table into an actual table with entries.
        Has to be called after initialization of all tables because it needs to make use of the
        complete table_registry to link up entries with other tables."""

        if not self.raw_content:
            raise EmptyTableException(self.name + " contains no entries")

        for raw_entry in self.raw_content:
            if not Table.is_entry_numbering_valid(raw_entry):
                raise InvalidEntryNumberingException("Table " + self.name
                                                     + " contains incorrectly numbered entry " 
                                                     + raw_entry)

            single_entry = re.search(Table.ENTRY_SINGLE_NUMBER_REGEX, raw_entry)
            range_entry = re.search(Table.ENTRY_RANGE_REGEX, raw_entry)


            if single_entry is not None:
                entry_nr = int(single_entry.group(1))
                entry_value = single_entry.group(2)
                if entry_nr in self.content:
                    raise DuplicateEntryException(self.name + ": Entry number " + str(entry_nr)
                                                  + " is used more than once")
                self.content[entry_nr] = Entry(entry_value, table_registry)
                if entry_nr > self.table_size:
                    self.table_size = entry_nr
            elif range_entry is not None:
                entry_range_str = range_entry.group(1).split("-")
                entry_range = range(int(entry_range_str[0]), int(entry_range_str[1]) + 1)
                entry_range_value = range_entry.group(2)
                for i in entry_range:
                    if i in self.content:
                        raise DuplicateEntryException(self.name + ": " + str(i)
                                                      + " is used more than once")
                    self.content[i] = Entry(entry_range_value, table_registry)
                    if i > self.table_size:
                        self.table_size = i


    def to_string(self):
        """Returns the table as a string"""

        string = "\n\n"
        string += self.name

        for key in self.content:
            entry_string = str(key) + ": " + self.content[key].to_string()
            string += "\n" + entry_string

        return string

    def generate_result(self):
        """Rolls on the table, generating and returning a single result as string"""
        if not self.content:
            raise TableNotYetParsedException()
        random_number = random.randint(1, self.table_size)
        return self.content[random_number].get_entry()


class Entry:
    """Individual entries within a table of a randomizer. Can contain links to other tables."""

    def __init__(self, entry_value, table_registry):
        def create_subtable(content):     
            subtable_name = "<<Entry_" + str(self.__hash__()) + ">>"
            content_array = content.split(",")
            subtable_raw = [subtable_name]
            for entry in content_array:
                subtable_raw.append(entry.strip())

            subtable = Table(subtable_raw)
            subtable.parse_raw_content(table_registry)
            return subtable

        value_split = entry_value.split("-->", 1)
        self.text_value = value_split[0].strip()
        self.subtable_value = None

        if len(value_split) > 1:
            if not value_split[1]:
                raise UnclearSubEntryException("Entry >" + entry_value + "< is unclear.\n"
                                               + "--> must always be followed by something")
            subtable_raw = value_split[1].strip()
            if subtable_raw[0] == "[":
                if subtable_raw[-1:] != "]":
                    raise UnclearSubEntryException("Entry >" + entry_value + "< is unclear.\n"
                                                   + "Subtable Entries must start and end with [],"
                                                   + "Linked tables must not start or end with []")
                self.subtable_value = create_subtable(subtable_raw.strip("[").strip("]"))
            else:
                if subtable_raw not in table_registry:
                    raise MissingTableException("Table " + subtable_raw + " not found")
                self.subtable_value = table_registry[subtable_raw]


    def to_string(self):
        """Returns entry as a string"""

        return_string = self.text_value
        if self.subtable_value is not None:
            return_string += "--> ["
            subtable_strings = self.subtable_value.to_string().split("\n")
            subtable_strings = [value for value in subtable_strings if value != ""]

            for entry in subtable_strings[1:]:
                return_string += entry + ", "
            return_string = return_string.strip(", ")
            return_string += "]"
        return return_string

    def get_entry(self):
        """Generates and returns the entry value from the text and, if present, the linked/subtable"""

        result_string = self.text_value
        if self.subtable_value is not None:
            result_string += ": " + self.subtable_value.generate_result()
        return result_string
