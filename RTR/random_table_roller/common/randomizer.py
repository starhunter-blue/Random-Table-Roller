"""Encloses the Randomizer class"""
from random_table_roller.common.exceptions import FaultyRandomizerException
from random_table_roller.common.table import Table

class Randomizer:
    """Random generator with one or more tables to be rolled on"""

    def __init__(self, name, raw_tables):
        self.name = name
        self.table_registry = {}

        for raw_table in raw_tables:
            table = Table(raw_table.split("\n"))
            self.table_registry[table.name.strip("<").strip(">")] = table

        for table_name in self.table_registry:
            self.table_registry[table_name].parse_raw_content(self.table_registry)

    def to_string(self):
        """Turns the random generator and all contained tables into a string"""
        string = self.name
        for key in self.table_registry:
            string += self.table_registry[key].to_string()

        return string

    def set_name(self, name):
        """Sets the name of the generator to the provided string"""
        self.name = name

    def add_table(self, table):
        """Adds a table to the generator.
        Tables must be provided as a string. The first line is the name of the table and must be
        enclosed in <> or <<>> to denote a regular table or a subtable."""
        if not table:
            raise FaultyRandomizerException("Element was empty")

        lines = table.split("\n")
        if len(lines) <= 1:
            raise FaultyRandomizerException(lines[0] + " is not followed by a table")

        table_name = lines[0]

        if not (table_name[0] == "<" and table_name[1] != "<" and table_name[-1] == ">" and table_name[-2] != ">"):
            if not (table_name[0] == "<" and table_name[1] == "<" and table_name[-1] == ">" and table_name[-2] == ">"):
                raise FaultyRandomizerException(table_name + " is not identifiable, missing or incoherent use of </<< or >/>>")

    def randomize(self, number_of_results=1):
        """Creates a number of randomzations from the randomizer equal to
         number_of_results or 1 if none is provided"""
        
        total_results_string = ""
        for i in range(number_of_results):
            results_string = self.name + " Result\n"

            for table_name in self.table_registry:
                if self.table_registry[table_name].subtable == True:
                    continue
                results_string += "\n<" + table_name + ">"
                results_string += "\n" + self.table_registry[table_name].generate_result() + "\n"

            if number_of_results > 1:
                total_results_string = "\nResult " + i+1 + "\n"
            total_results_string += results_string

        return total_results_string
