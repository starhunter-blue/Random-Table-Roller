import PySimpleGUI as sg
import sys

def run():
      if len(sys.argv) == 1:
            fname = sg.PopupGetFile(message = "Open Random Table", file_types= (("All Files", "*.*"), ("Text Files", ".txt")))
      else:
            fname = sys.argv[1]

      if not fname:
            sg.Popup("Cancel", "No filename supplied")
            raise SystemExit("Cancelling: no filename supplied")
      else:
            sg.Popup('The filename you chose was', fname)