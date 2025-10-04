import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox,
    QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

import requests

API_URL = "http://127.0.0.1:5000"

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 150)

        main_layout = QVBoxLayout()
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        login_label_layout = QHBoxLayout()
        login_label_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        login_label = QLabel("Login")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        login_label.setFont(font)
        login_label.setAlignment(Qt.AlignCenter)
        login_label_layout.addWidget(login_label)
        login_label_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(login_label_layout)

        user_label_layout = QHBoxLayout()
        user_label_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        user_label = QLabel("Nome de usuário:")
        user_label.setAlignment(Qt.AlignCenter)
        user_label_layout.addWidget(user_label)
        user_label_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(user_label_layout)

        user_input_layout = QHBoxLayout()
        user_input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Usuário")
        self.username_input.setMaximumWidth(200)
        self.username_input.setAlignment(Qt.AlignCenter)
        user_input_layout.addWidget(self.username_input)
        user_input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(user_input_layout)

        pass_label_layout = QHBoxLayout()
        pass_label_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        pass_label = QLabel("Senha:")
        pass_label.setAlignment(Qt.AlignCenter)
        pass_label_layout.addWidget(pass_label)
        pass_label_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(pass_label_layout)

        pass_input_layout = QHBoxLayout()
        pass_input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Senha")
        self.password_input.setMaximumWidth(200)
        self.password_input.setAlignment(Qt.AlignCenter)
        self.password_input.setEchoMode(QLineEdit.Password)
        pass_input_layout.addWidget(self.password_input)
        pass_input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(pass_input_layout)

        button_layout = QHBoxLayout()
        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        enter_button = QPushButton("Entrar", self)
        enter_button.clicked.connect(self.login)
        button_layout.addWidget(enter_button)

        register_button = QPushButton("Registrar", self)
        register_button.clicked.connect(self.register) 
        button_layout.addWidget(register_button) 

        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(button_layout)

        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(main_layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Erro ao Entrar", "Todos os campos devem ser preenchidos.",)
            return

        try:
            response = requests.post(f"{API_URL}/user/login", json={"username": username, "password": password})
            if response.status_code == 200:
                QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
            else:
                QMessageBox.warning(self, "Erro", "Falha no login. Verifique suas credenciais.")

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Erro", f"Erro de conexão: {e}")

    def register(self):
        username= self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Erro ao se Registrar", "Todos os campos devem ser preenchidos.")
            return

        try:
            response = requests.post(f"{API_URL}/user/register", json={"username": username, "password": password})
            if response.status_code == 200:
                QMessageBox.information(self, "Sucesso", "Registro bem-sucedido! Você já pode fazer login.")
            
            else:
                QMessageBox.warning(self, "Erro", "Falha no registro. Tente um nome de usuário diferente.")
            
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Erro", f"Erro de conexão: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.showMaximized()
    sys.exit(app.exec_())
