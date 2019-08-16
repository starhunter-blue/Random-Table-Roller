from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QMessageBox


class GUI:

    def __init__(self):
        self.app = QApplication([])
    
    def set_callback(self, callback):
        self.callback = callback
    
    def display(self):
        window = QWidget()
        window.setWindowTitle("Random Table Roller")

        layout = QVBoxLayout()

        load_table_button = QPushButton("Import Table")
        load_table_button.clicked.connect(self.clicked_load)
        layout.addWidget(load_table_button)

        randomize_button = QPushButton("Randomize!")
        randomize_button.clicked.connect(self.clicked_randomize)
        layout.addWidget(randomize_button)

        save_button = QPushButton("Save Results")
        save_button.clicked.connect(self.clicked_save)
        layout.addWidget(save_button)

        window.setLayout(layout)
        window.show()

        self.app.exec_()
    
    def clicked_load(self):
        filename = QFileDialog.getOpenFileName(filter = "Text Files (*.txt) ;; All Files (*.*)")[0]
        if filename:
            self.on_button_clicked("load", filename)

    def clicked_randomize(self):
        self.on_button_clicked("randomize")

    def clicked_save(self):
        file_dialog = QFileDialog()
        filename = file_dialog.getSaveFileName(filter = "Text Files (*.txt) ;; All Files (*.*)")[0]
        self.on_button_clicked("save", filename)

    def on_button_clicked(self, event, filename = None):
        self.callback(event, filename)

    def save_results(self):
        file_dialog = QFileDialog()
        file_dialog.getSaveFileName()

    def show_empty_file_loaded_error(self):
        alert = QMessageBox()
        alert.setWindowTitle("Error")
        alert.setIcon(QMessageBox.Critical)
        alert.setText("Loaded file was empty")
        alert.exec_()