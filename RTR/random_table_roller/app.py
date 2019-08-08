from random_table_roller.interface.gui import GUI
from random_table_roller import USER_INTERFACE

def run():
    USER_INTERFACE.set_callback(callback)

    USER_INTERFACE.display()

def callback(event, filename):
    print("Button Event: %s" % event)

    if event == "load":
        print(filename)

    if event == "save":
        print(filename)

