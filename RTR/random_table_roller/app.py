import PySimpleGUI as sg

def run():
    layout = [[sg.Text("Random Table")],
              [sg.In(), sg.FileBrowse(file_types = (("Text Files", ".txt"), ("All Files", "*.*")))],
              [sg.Open(), sg.Cancel()]]
    
    window = sg.Window("Random Table Roller", layout)
    event, values = window.Read()
    window.Close()

    file_name = values[0]
    print(event, values)

    if not file_name:
        sg.Popup("Cancel", "No filename1 supplied")
        raise SystemExit("Cancelling: No filename supplied")
    else:
        sg.Popup("The filename was", file_name)
