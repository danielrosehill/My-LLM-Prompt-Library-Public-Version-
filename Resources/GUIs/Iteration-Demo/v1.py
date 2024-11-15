import sys
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QTextEdit, QPushButton, QFileDialog, QMessageBox)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt, QSettings

class PromptOutputGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Prompt and Output Saver')
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial;
            }
            QLineEdit, QTextEdit {
                background-color: white;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        layout = QVBoxLayout()

        # Title input
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter title")
        layout.addWidget(self.title_input)

        # Prompt input
        self.prompt_input = QTextEdit()
        self.prompt_input.setPlaceholderText("Enter prompt")
        layout.addWidget(self.prompt_input)

        # Output input
        self.output_input = QTextEdit()
        self.output_input.setPlaceholderText("Enter output")
        layout.addWidget(self.output_input)

        # Buttons for setting paths
        path_layout = QHBoxLayout()
        self.prompt_path_button = QPushButton("Set Prompt Path")
        self.output_path_button = QPushButton("Set Output Path")
        path_layout.addWidget(self.prompt_path_button)
        path_layout.addWidget(self.output_path_button)
        layout.addLayout(path_layout)

        # Save button
        self.save_button = QPushButton("Save to Library")
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        # Connect buttons to functions
        self.prompt_path_button.clicked.connect(self.set_prompt_path)
        self.output_path_button.clicked.connect(self.set_output_path)
        self.save_button.clicked.connect(self.save_to_library)

        # Load saved paths
        self.settings = QSettings("PromptOutputApp", "Paths")
        self.prompt_path = self.settings.value("prompt_path", "")
        self.output_path = self.settings.value("output_path", "")

    def set_prompt_path(self):
        path = QFileDialog.getExistingDirectory(self, "Select Prompt Directory")
        if path:
            self.prompt_path = path
            self.settings.setValue("prompt_path", path)

    def set_output_path(self):
        path = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if path:
            self.output_path = path
            self.settings.setValue("output_path", path)

    def save_to_library(self):
        title = self.title_input.text()
        prompt = self.prompt_input.toPlainText()
        output = self.output_input.toPlainText()

        if not title or not prompt or not output:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        if not self.prompt_path or not self.output_path:
            QMessageBox.warning(self, "Path Error", "Please set both prompt and output paths.")
            return

        file_name = self.prettify_title(title) + ".md"

        # Save output file
        output_file_path = os.path.join(self.output_path, file_name)
        with open(output_file_path, 'w') as f:
            f.write(f"# Prompt\n\n{prompt}\n\n# Output\n\n{output}")

        # Save prompt file
        prompt_file_path = os.path.join(self.prompt_path, file_name)
        with open(prompt_file_path, 'w') as f:
            f.write(f"# Prompt\n\n{prompt}")

        QMessageBox.information(self, "Success", "Prompt and output saved.")
        self.clear_inputs()

    def prettify_title(self, title):
        return title.lower().replace(" ", "-")

    def clear_inputs(self):
        self.title_input.clear()
        self.prompt_input.clear()
        self.output_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PromptOutputGUI()
    ex.show()
    sys.exit(app.exec())