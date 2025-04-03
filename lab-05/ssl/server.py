import socket
import ssl
import threading

# Địa chỉ và cổng của server
SERVER_ADDRESS = ('localhost', 12345)

# Danh sách quản lý các client
clients = []

def handle_client(client_socket):
    """Xử lý kết nối từ một client cụ thể"""
    try:
        while True:
            # Nhận dữ liệu từ client
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Nhận được: {data.decode('utf-8')}")

            # Gửi dữ liệu đến các client khác
            for client in clients:
                if client != client_socket:
                    client.send(data)
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        # Ngắt kết nối và xóa client
        clients.remove(client_socket)
        client_socket.close()

# Hàm chính khởi động server
def start_server():
    # Tạo socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(5)
    print("Server đang chờ kết nối...")

    try:
        while True:
            # Chấp nhận kết nối từ client
            client_socket, client_address = server_socket.accept()
            print(f"Đã kết nối với: {client_address}")

            # Cấu hình SSL
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(certfile="./certificates/server-cert.crt",
                                     keyfile="./certificates/server-key.key")

            # Bọc socket với SSL
            ssl_socket = context.wrap_socket(client_socket, server_side=True)

            # Thêm client vào danh sách
            clients.append(ssl_socket)

            # Tạo luồng mới xử lý client
            client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
            client_thread.start()
    except Exception as e:
        print(f"Lỗi server: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
