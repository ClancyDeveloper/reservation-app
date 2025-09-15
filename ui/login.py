import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QImage

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Teste")
window.setGeometry(100,100,400,300)

texto = QLabel('Texto muito foda', window)
texto.setGeometry(10,10,100,30)

imagem = QImage("assets/image.png")

icon = QIcon("assets/image.png")
window.setWindowIcon(icon)

window.show()

sys.exit(app.exec())
