from random_table_roller.common.exceptions import FaultyRandomizerException
import re

class Randomizer:
    
    def __init__(self):
        name = ""
        tables = {}

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