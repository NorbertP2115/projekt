from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog

class ConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.open_button = QPushButton("Open File")
        self.save_button = QPushButton("Save File")

        self.open_button.clicked.connect(self.open_file)
        self.save_button.clicked.connect(self.save_file)

        layout.addWidget(self.open_button)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.setWindowTitle("Data Converter")

    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;JSON Files (*.json);;YAML Files (*.yaml);;XML Files (*.xml)", options=options)
        if file_path:
            print(f"Selected file: {file_path}")

    def save_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;JSON Files (*.json);;YAML Files (*.yaml);;XML Files (*.xml)", options=options)
        if file_path:
            print(f"File to save: {file_path}")

if __name__ == "__main__":
    app = QApplication([])
    ui = ConverterUI()
    ui.show()
    app.exec_()
