import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class ColorSwitcher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Switcher 🎨")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Klik tombol untuk ubah warna!", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 16px;")

        # Tombol warna
        self.red_btn = QPushButton("Merah")
        self.green_btn = QPushButton("Hijau")
        self.blue_btn = QPushButton("Biru")
        self.random_btn = QPushButton("Random 🎲")
# Hubungkan tombol ke fungsi
        self.red_btn.clicked.connect(lambda: self.change_color("red"))
        self.green_btn.clicked.connect(lambda: self.change_color("green"))
        self.blue_btn.clicked.connect(lambda: self.change_color("blue"))
        self.random_btn.clicked.connect(self.random_color)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.red_btn)
        layout.addWidget(self.green_btn)
        layout.addWidget(self.blue_btn)
        layout.addWidget(self.random_btn)
        self.setLayout(layout)

    def change_color(self, color):
        self.setStyleSheet(f"background-color: {color};")
        self.label.setText(f"Warna diubah ke: {color.capitalize()}")

    def random_color(self):
        r = lambda: random.randint(0,255)
        color = f"rgb({r()},{r()},{r()})"
        self.setStyleSheet(f"background-color: {color};")
        self.label.setText(f"Warna diubah ke random 🎲")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorSwitcher()
    window.show()
    sys.exit(app.exec_())
