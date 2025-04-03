import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    """
    Lớp WebSocketClient thực hiện kết nối và giao tiếp với server.
    """
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    def start(self):
        """
        Bắt đầu kết nối và đọc từ server.
        """
        self.connect_and_read()

    def stop(self):
        """
        Dừng vòng lặp I/O.
        """
        self.io_loop.stop()

    def connect_and_read(self):
        """
        Kết nối với server WebSocket và thiết lập callback để xử lý thông điệp.
        """
        print("Đang kết nối để đọc dữ liệu...")
        tornado.websocket.websocket_connect(
            url="ws://localhost:8888/websocket/",
            callback=self.handle_connection,
            on_message_callback=self.on_message,
            ping_interval=10,
            ping_timeout=30,
        )

    def handle_connection(self, future):
        """
        Xử lý kết quả kết nối và thiết lập lại nếu không thành công.
        """
        try:
            self.connection = future.result()
        except Exception:
            print("Kết nối không thành công, thử lại sau 3 giây...")
            self.io_loop.call_later(3, self.connect_and_read)

    def on_message(self, message):
        """
        Xử lý thông điệp nhận được từ server.
        """
        if message is None:
            print("Mất kết nối, đang thử lại...")
            self.connect_and_read()
            return

        print(f"Nhận được thông điệp từ server: {message}")
        self.connection.read_message(callback=self.on_message)

def main():
    """
    Hàm chính thiết lập vòng lặp I/O và khởi chạy WebSocket client.
    """
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    io_loop.add_callback(client.start)

    io_loop.start()

if __name__ == "__main__":
    main()
