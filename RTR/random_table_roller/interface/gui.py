import random_table_roller.fix_qt_import_error
from PyQt5.QtWidgets import QApplication, \
                            QWidget, \
                            QPushButton, \
                            QVBoxLayout, \
                            QFileDialog, \
                            QMessageBox, \
                            QTextEdit


class GUI:
    """Graphical Interface for user interaction"""

    def __init__(self):
        self.app = QApplication([])

    def set_callback(self, callback):
        """Sets the callback to notify the controller of user interaction"""
        self.callback = callback
    
    def display(self):
        """Displays the GUI"""

        window = QWidget()
        window.setWindowTitle("Random Table Roller")

        layout = QVBoxLayout()

        load_table_button = QPushButton("Import Randomizer")
        load_table_button.clicked.connect(self.clicked_load)
        layout.addWidget(load_table_button)

        randomize_button = QPushButton("Randomize!")
        randomize_button.clicked.connect(self.clicked_randomize)
        layout.addWidget(randomize_button)

        save_button = QPushButton("Save Results")
        save_button.clicked.connect(self.clicked_save)
        layout.addWidget(save_button)

        self.text_field = QTextEdit()
        self.text_field.setText("Ready to Randomize!")
        layout.addWidget(self.text_field)

        window.setLayout(layout)
        window.show()

        self.app.exec_()

    def clicked_load(self):
        """Function to be called by Load Table Button"""

        filename = QFileDialog.getOpenFileName(filter="Text Files (*.txt) ;; All Files (*.*)")[0]
        if filename:
            self.on_button_clicked("load", filename)

    def clicked_randomize(self):
        """Function to be called by Randomize Button"""

        self.on_button_clicked("randomize")

    def clicked_save(self):
        """Function to be called by Save Button"""

        file_dialog = QFileDialog()
        filename = file_dialog.getSaveFileName(filter="Text Files (*.txt) ;; All Files (*.*)")[0]
        self.on_button_clicked("save", filename)

    def on_button_clicked(self, event, filename=None):
        self.callback(event, filename)

    def save_results(self):
        file_dialog = QFileDialog()
        file_dialog.getSaveFileName()

    def show_error(self, message):
        alert = QMessageBox()
        alert.setWindowTitle("Error")
        alert.setIcon(QMessageBox.Critical)
        alert.setText(message)
        alert.exec_()

    def update_textbox(self, message):
        """Updates the textbox with randomization results"""

        self.text_field.setText(message)

    def get_text_field_content(self):
        """Returns the text contained in the text field"""
        return self.text_field.toPlainText()