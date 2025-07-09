import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QComboBox, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter, ImageEnhance
import io

class ImageUploader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Upload dan Edit Foto")
        self.resize(500, 500)

        self.label = QLabel("Klik tombol untuk upload foto", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedSize(400, 400)
        self.label.setStyleSheet("background-color: gray; font-size: 16px")

        self.button_upload = QPushButton("Upload Foto", self)
        self.button_upload.clicked.connect(self.upload_image)
        self.button_upload.setStyleSheet("background-color: lavender; font-size: 16px")
        self.combo_filter = QComboBox(self)
        self.combo_filter.addItem("Normal")
        self.combo_filter.addItem("Greyscale")
        self.combo_filter.addItem("Sharpen")
        self.combo_filter.currentIndexChanged.connect(self.apply_filter)
        self.combo_filter.setEnabled(False)  # Disable
        self.combo_filter.setStyleSheet("background-color: blue; font-size: 16px")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_upload)
        layout.addWidget(self.combo_filter)

        self.setLayout(layout)

        self.original_image = None  # Simpan PIL image asli
    def upload_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Pilih Foto", "", "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
        if file_name:
            try:
                self.original_image = Image.open(file_name)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Gagal membuka gambar:\n{str(e)}")
                return

            self.show_image(self.original_image)
            self.combo_filter.setCurrentIndex(0)  # Reset ke normal
            self.combo_filter.setEnabled(True)
    def show_image(self, pil_image):
            # Convert PIL Image ke QPixmap
            data = io.BytesIO()
            pil_image.save(data, format='PNG')
            data.seek(0)
            qimage = QImage.fromData(data.read())
            pixmap = QPixmap.fromImage(qimage)
            pixmap = pixmap.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label.setPixmap(pixmap)
    def apply_filter(self, index):
            if self.original_image is None:
                return

            if index == 0:  # Normal
                img = self.original_image
            elif index == 1:  # Greyscale
                img = self.original_image.convert('L').convert('RGBA')
            elif index == 2:  # Sharpen
                img = self.original_image.filter(ImageFilter.SHARPEN)
                enhancer = ImageEnhance.Sharpness(self.original_image)
                pic_sharp = enhancer.enhance(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)  # 2.0 = 2x lebih tajam
                img = pic_sharp
            self.show_image(img)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageUploader()
    window.show()
    sys.exit(app.exec_())
