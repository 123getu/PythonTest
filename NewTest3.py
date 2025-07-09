from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QFileDialog, QLabel
)
from PIL import Image, ImageFilter

class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Editor Menu with Image Picker")
        self.setGeometry(300, 300, 400, 200)

        self.image_path = None  # Path gambar sementara

        layout = QVBoxLayout()

        # Label buat nampilin path gambar
        self.label_path = QLabel("Belum ada gambar dipilih")
        layout.addWidget(self.label_path)

        # Tombol pilih gambar
        self.btn_select = QPushButton("Pilih Gambar")
        self.btn_select.clicked.connect(self.select_image)
        layout.addWidget(self.btn_select)

        # ComboBox menu efek
        self.combo = QComboBox()
        self.combo.addItems(["Show Original", "Rotate 90°", "Blur"])
        layout.addWidget(self.combo)
# Tombol Apply
        self.btn_apply = QPushButton("Apply Effect")
        self.btn_apply.clicked.connect(self.apply_effect)
        layout.addWidget(self.btn_apply)

        self.setLayout(layout)

    def select_image(self):
        file_name, c = QFileDialog.getOpenFileName(self, "Pilih Gambar", "", "Images (*.png *.jpg *.jpeg *.bmp)") #only file_name that will be used
        if file_name:
            self.image_path = file_name
            self.label_path.setText(f"Gambar: {self.image_path}")
    def apply_effect(self):
        if not self.image_path:
            self.label_path.setText("Pilih gambar dulu!")
            return

        selected = self.combo.currentText()

        if selected == "Show Original":
            img = Image.open(self.image_path)
            img.show()


        elif selected == "Rotate 90°":
            img = Image.open(self.image_path).transpose(Image.ROTATE_90)
            img.show()

        elif selected == "Blur":
            img = Image.open(self.image_path).filter(ImageFilter.GaussianBlur(5))
            img.show()
if __name__ == "__main__":
    app = QApplication([])
    window = ImageEditor()
    window.show()
    app.exec_()