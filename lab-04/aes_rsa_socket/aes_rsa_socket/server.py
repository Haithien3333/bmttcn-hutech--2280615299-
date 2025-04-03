# Thư viện cần thiết
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

# Khởi tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

# Tạo cặp khóa RSA
server_key = RSA.generate(2048)

# Danh sách các client kết nối
clients = []

# Hàm mã hóa thông điệp
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

# Hàm giải mã thông điệp
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# Hàm xử lý kết nối từ client
def handle_client(client_socket, client_address):
    print(f"Kết nối từ {client_address}")

    # Gửi khóa RSA công khai của server cho client
    client_socket.send(server_key.publickey().export_key(format='PEM'))

    # Nhận khóa RSA công khai từ client
    client_received_key = RSA.import_key(client_socket.recv(2048))
# Tạo khóa AES để mã hóa thông điệp
    aes_key = get_random_bytes(16)

# Mã hóa khóa AES bằng khóa công khai của client
    cipher_rsa = PKCS1_OAEP.new(client_received_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypted_aes_key)

# Lưu trữ client vào danh sách
    clients.append((client_socket, aes_key))

# Xử lý luồng thông điệp từ client
    while True:
        encrypted_message = client_socket.recv(1024)
        decrypted_message = decrypt_message(aes_key, encrypted_message)
        print(f"Nhận từ {client_address}: {decrypted_message}")

    # Gửi thông điệp cho các client khác
        for client, key in clients:
            if client != client_socket:
                encrypted = encrypt_message(key, decrypted_message)
                client.send(encrypted)

    # Thoát nếu nhận được thông điệp "exit"
        if decrypted_message == "exit":
            break

    clients.remove((client_socket, aes_key))
    client_socket.close()
    print(f"Kết nối với {client_address} đã đóng")

# Chấp nhận kết nối từ client mới
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
