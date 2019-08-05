import PySimpleGUI as sg

def run():
    layout = [[sg.Text("Random Table")],
              [sg.In(), sg.FileBrowse(file_types = (("Text Files", ".txt"), ("All Files", "*.*")))],
              [sg.Button(button_text="Randomize!"), sg.Exit()]]
              
    
    window = sg.Window("Random Table Roller", layout)
    
    while True:
        event, values = window.Read()
        if event is "Randomize!":
            f = sg.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            f.write("Test")
            f.close()
        if event is None or "Exit":
            break
        print(event, values)
    
    window.Close()
    

    file_name = values[0]
    print(event, values)

    if not file_name:
        sg.Popup("Cancel", "No filename1 supplied")
        raise SystemExit("Cancelling: No filename supplied")
    else:
        sg.Popup("The filename was", file_name)
