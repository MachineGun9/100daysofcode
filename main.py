import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QGridLayout


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 350)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_ui()

    def create_ui(self):
        self.result_display = QLineEdit()
        self.layout.addWidget(self.result_display)

        self.buttons = QGridLayout()

        buttons_layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row, buttons_row in enumerate(buttons_layout):
            for col, button_value in enumerate(buttons_row):
                button = QPushButton(button_value)
                button.clicked.connect(self.on_button_click)
                self.buttons.addWidget(button, row, col)

        self.layout.addLayout(self.buttons)

    def on_button_click(self):
        button = self.sender()
        current_text = self.result_display.text()
        button_text = button.text()

        if button_text == '=':
            try:
                result = eval(current_text)
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText('Error')
        else:
            new_text = current_text + button_text
            self.result_display.setText(new_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
