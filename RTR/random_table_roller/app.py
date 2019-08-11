from random_table_roller.interface.gui import GUI
from random_table_roller import USER_INTERFACE
from random_table_roller.common.exceptions import FileEmptyException

def run():
    USER_INTERFACE.set_callback(callback)

    USER_INTERFACE.display()

def callback(event, filename):
    print("Button Event: %s" % event)

    try:
        if event == "load":
            loaded_table = load_table(filename)
            if not loaded_table[0]:
                raise FileEmptyException
            print(loaded_table[0])

        if event == "save":
            print(filename)

    except FileEmptyException:
        USER_INTERFACE.show_empty_file_loaded_error()

def load_table(filename):
    with open(filename, "r") as file:
        if file.mode == "r":
            return file.read().split("\n")

