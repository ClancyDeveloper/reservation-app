import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

API_URL = "http://127.0.0.1:5000"

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Usuário")
        layout.addWidget(QLabel("Nome de usuário:"))
        layout.addWidget(self.username_input)
        self.username_input.setGeometry(525, 300, 200, 20)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Senha")
        layout.addWidget(QLabel("Senha:"))
        layout.addWidget(self.password_input)
        self.password_input.setGeometry(525, 330, 200, 20)

        self.login_text = QLabel("Login")
        self.login_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.login_text)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.showMaximized()
    sys.exit(app.exec_())
        