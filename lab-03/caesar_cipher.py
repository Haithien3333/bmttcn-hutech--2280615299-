import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        
        try:
            key = int(self.ui.txt_key.toPlainText())  # Đảm bảo key là số
        except ValueError:
            QMessageBox.critical(self, "Error", "Key must be a number!")
            return

        payload = {
            "plain_text": self.ui.txt_plain.toPlainText(),
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher.setPlainText(data["encrypted_message"])
                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                QMessageBox.critical(self, "Error", f"API Error: {response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request Error: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        
        try:
            key = int(self.ui.txt_key.toPlainText())  # Đảm bảo key là số
        except ValueError:
            QMessageBox.critical(self, "Error", "Key must be a number!")
            return

        payload = {
            "cipher_text": self.ui.txt_cipher.toPlainText(),
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain.setPlainText(data["decrypted_message"])
                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                QMessageBox.critical(self, "Error", f"API Error: {response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
