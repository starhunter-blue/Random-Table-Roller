from random_table_roller.common.exceptions import FaultyRandomizerException
from random_table_roller.common.table import Table
import re

class Randomizer:
    
    def __init__(self, name, raw_tables):
        self.name = name
        self.table_registry = {}

        for raw_table in raw_tables:
            table = Table(raw_table.split("\n"))
            self.table_registry[table.name] = table

        print(self.table_registry)

    def to_string(self):
        string = self.name
        print(self.table_registry["<Table 1>"].to_string())
        for key in self.table_registry:
            string += self.table_registry[key].to_string()

        return string

    def set_name(self, name):
        self.name = name

    def add_table(self, table):
        if not table:
            raise FaultyRandomizerException("Element was empty")

        lines = table.split("\n")
        if len(lines) <= 1:
            raise FaultyRandomizerException(lines[0] + " is not followed by a table")

        table_name = lines[0]
        
        if not (table_name[0] == "<" and table_name[1] != "<" and table_name[-1] == ">" and table_name[-2] != ">"):
            if not (table_name[0] == "<" and table_name[1] == "<" and table_name[-1] == ">" and table_name[-2] == ">"):
                raise FaultyRandomizerException(table_name + " is not identifiable, missing or incoherent use of </<< or >/>>")