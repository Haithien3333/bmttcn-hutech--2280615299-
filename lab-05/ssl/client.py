import socket
import ssl
import threading

# Địa chỉ và cổng của server
SERVER_ADDRESS = ('localhost', 12345)

def receive_data(ssl_socket):
    """Hàm xử lý nhận dữ liệu từ server."""
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhận được:", data.decode('utf-8'))
    except Exception as e:
        print("Lỗi khi nhận dữ liệu:", e)
    finally:
        ssl_socket.close()
        print("Kết nối đã đóng.")

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tạo SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.verify_mode = ssl.CERT_NONE  # Có thể tùy chỉnh theo nhu cầu
context.check_hostname = False  # Có thể tùy chỉnh theo nhu cầu

# Thiết lập kết nối SSL
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
ssl_socket.connect(SERVER_ADDRESS)

# Tạo luồng để nhận dữ liệu từ server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()


try:
    while True:
        # Nhập dữ liệu từ bàn phím
        message = input("Nhập tin nhắn: ")
        if message.lower() == 'exit':
            break
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    print("Đã ngắt kết nối.")
    pass 
finally:
    ssl_socket.close()
   