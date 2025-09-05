import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QToolBar,
    QMessageBox,
)
from PySide6.QtCore import Qt


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)

        # Add toolbar
        self.toolbar = QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        self.layout.addWidget(self.display, 0, 0, 1, 4)

        # Button layout
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
            ("C", 5, 0, 1, 4),
        ]

        # Create and add buttons
        for btn_text, row, col, *span in buttons:
            button = QPushButton(btn_text)
            button.setFixedSize(60, 60)
            if btn_text == "C":
                button.clicked.connect(self.clear_display)
                self.layout.addWidget(button, row, col, span[0], span[1])
            elif btn_text == "=":
                button.clicked.connect(self.calculate)
                self.layout.addWidget(button, row, col)
            else:
                button.clicked.connect(
                    lambda _, text=btn_text: self.add_to_display(text)
                )
                self.layout.addWidget(button, row, col)

        self.current_expression = ""

    def show_about_dialog(self):
        """Show an About dialog with information about the calculator."""
        QMessageBox.about(
            self,
            "About Calculator",
            "Simple Calculator v0.0.1\n"
            "A basic arithmetic calculator built with PySide6.\n"
            "Supports addition, subtraction, multiplication, and division.\n"
            "Created in 2025.",
        )

    def add_to_display(self, text):
        self.current_expression += text
        self.display.setText(self.current_expression)

    def clear_display(self):
        self.current_expression = ""
        self.display.setText("")

    def evaluate_expression(self, expression):
        """Evaluate an arithmetic expression using a stack-based approach."""
        try:
            # Split expression into tokens
            tokens = []
            num = ""
            for char in expression:
                if char in "+-*/":
                    if num:
                        tokens.append(float(num))
                        num = ""
                    tokens.append(char)
                else:
                    num += char
            if num:
                tokens.append(float(num))

            # Process multiplication and division first
            result = []
            i = 0
            while i < len(tokens):
                if tokens[i] in ["*", "/"] and i > 0 and i < len(tokens) - 1:
                    left = result.pop() if result else tokens[i - 1]
                    right = tokens[i + 1]
                    if tokens[i] == "*":
                        result.append(left * right)
                    elif tokens[i] == "/":
                        if right == 0:
                            return None
                        result.append(left / right)
                    i += 2
                else:
                    result.append(tokens[i])
                    i += 1

            # Process addition and subtraction
            total = result[0]
            i = 1
            while i < len(result):
                if result[i] == "+":
                    total += result[i + 1]
                elif result[i] == "-":
                    total -= result[i + 1]
                i += 2

            # Format result to avoid floating-point precision issues
            return round(total, 10)
        except (ValueError, IndexError):
            return None

    def calculate(self):
        result = self.evaluate_expression(self.current_expression)
        if result is not None:
            self.display.setText(str(result))
            self.current_expression = str(result)
        else:
            self.display.setText("Error")
            self.current_expression = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
