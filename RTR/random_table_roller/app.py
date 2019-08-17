import re
from random_table_roller.interface.gui import GUI
from random_table_roller import USER_INTERFACE, randomizers, last_randomizer, last_result
from random_table_roller.common.exceptions import FileEmptyException, NoRandomizerLoadedException
from random_table_roller.common.randomizer import Randomizer

def run():
    """Starts the app"""
    USER_INTERFACE.set_callback(callback)
    USER_INTERFACE.display()

def callback(event, filename=None):
    """The callback function for the GUI to report user interaction events"""
    print("Button Event: %s" % event)

    try:
        if event == "load":
            loaded_randomizer = load_randomizer(filename)
            if not loaded_randomizer:
                raise FileEmptyException
            store_randomizer(loaded_randomizer)

        if event == "save":
            save_results(filename)

        if event == "randomize":
            if not last_randomizer:
                raise NoRandomizerLoadedException("No randomizer loaded")
            global last_result
            last_result = str(randomizers[last_randomizer].randomize())
            USER_INTERFACE.update_textbox(last_result)


    except FileEmptyException:
        USER_INTERFACE.show_error("Loaded file was empty")

    except NoRandomizerLoadedException:
        USER_INTERFACE.show_error("No randomizer loaded")

def load_randomizer(filename):
    """Loads up a randomizer file from the provided filename."""
    with open(filename, "r") as file:
        if file.mode == "r":
            return file.read()

def store_randomizer(randomizer):
    """Stores a parsed randomizer for use."""

    parsed_randomizer = parse_randomizer(randomizer)
    randomizers[parsed_randomizer.name] = parsed_randomizer
    global last_randomizer
    last_randomizer = parsed_randomizer.name

def parse_randomizer(randomizer):
    """Turns a raw text randomizer into a Randomizer object, ready for use."""

    blank_line_regex = r"(?:\r?\n){2,}"
    elements = re.split(blank_line_regex, randomizer.strip())
    parsed_randomizer = Randomizer(elements[0], elements[1:])

    return parsed_randomizer

def save_results(filename):
    """Saves the last generated randomization as a .txt"""

    with open(filename, "w+") as file:
        file.write(USER_INTERFACE.get_text_field_content())
