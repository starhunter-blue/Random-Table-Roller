from PyQt5.QtWidgets import QApplication, QWidget

class GUI:

    def __init__(self, callback):
        self.callback = callback
        self.app = QApplication([])
    
    def display(self):
        window = QWidget()
        window.setWindowTitle("Random Table Roller")
        window.show()
        self.app.exec_()
