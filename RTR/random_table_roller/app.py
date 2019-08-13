import re
from random_table_roller.interface.gui import GUI
from random_table_roller import USER_INTERFACE, randomizers
from random_table_roller.common.exceptions import FileEmptyException
from random_table_roller.common.randomizer import Randomizer

def run():
    USER_INTERFACE.set_callback(callback)
    
    USER_INTERFACE.display()

def callback(event, filename):
    print("Button Event: %s" % event)

    try:
        if event == "load":
            loaded_randomizer = load_randomizer(filename)
            if not loaded_randomizer:
                raise FileEmptyException
            store_randomizer(loaded_randomizer)

        if event == "save":
            print(filename)

    except FileEmptyException:
        USER_INTERFACE.show_empty_file_loaded_error()

def load_randomizer(filename):
    with open(filename, "r") as file:
        if file.mode == "r":
            return file.read()

def store_randomizer(randomizer):
    parsed_randomizer = parse_randomizer(randomizer)
    randomizers[randomizer.split("\n")[0]] = parsed_randomizer
    print(randomizers)

def parse_randomizer(randomizer):
    blank_line_regex = r"(?:\r?\n){2,}"
    elements = re.split(blank_line_regex, randomizer.strip())
    parsed_randomizer = Randomizer()
    parsed_randomizer.set_name(elements[0])

    for element in elements[1:]:
        parsed_randomizer.add_table(element)

    return parsed_randomizer

    

