import sys
import base64
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class EncoderDecoderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Encoder & Decoder")
        self.setGeometry(300, 150, 700, 500)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        title = QLabel("🔐 Encoder & Decoder Tool")
        title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter text here...")
        self.input_text.setFont(QFont("Consolas", 11))

        self.output_text = QTextEdit()
        self.output_text.setPlaceholderText("Output will appear here...")
        self.output_text.setFont(QFont("Consolas", 11))
        self.output_text.setReadOnly(True)

        button_layout = QHBoxLayout()

        encode_btn = QPushButton("Encode")
        decode_btn = QPushButton("Decode")
        clear_btn = QPushButton("Clear")

        encode_btn.clicked.connect(self.encode_text)
        decode_btn.clicked.connect(self.decode_text)
        clear_btn.clicked.connect(self.clear_text)

        button_layout.addWidget(encode_btn)
        button_layout.addWidget(decode_btn)
        button_layout.addWidget(clear_btn)

        main_layout.addWidget(title)
        main_layout.addWidget(QLabel("Input"))
        main_layout.addWidget(self.input_text)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(QLabel("Output"))
        main_layout.addWidget(self.output_text)

        self.setLayout(main_layout)
        self.apply_styles()

    def encode_text(self):
        try:
            text = self.input_text.toPlainText()
            encoded = base64.b64encode(text.encode()).decode()
            self.output_text.setText(encoded)
        except Exception as e:
            self.show_error(str(e))

    def decode_text(self):
        try:
            text = self.input_text.toPlainText()
            decoded = base64.b64decode(text).decode()
            self.output_text.setText(decoded)
        except Exception:
            self.show_error("Invalid Base64 input!")

    def clear_text(self):
        self.input_text.clear()
        self.output_text.clear()

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #ffffff;
            }
            QTextEdit {
                background-color: #1e1e1e;
                color: #ffffff;
                border-radius: 6px;
                padding: 10px;
            }
            QPushButton {
                background-color: #e50914;
                color: white;
                padding: 10px;
                font-size: 14px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #b20710;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncoderDecoderApp()
    window.show()
    sys.exit(app.exec())
