import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketServer(tornado.websocket.WebSocketHandler):
    """
    Lớp xử lý kết nối WebSocket server.
    """
    clients = set()  # Tập hợp lưu trữ các kết nối WebSocket từ client

    def open(self):
        """
        Thêm client mới vào danh sách khi kết nối WebSocket được mở.
        """
        WebSocketServer.clients.add(self)

    def on_close(self):
        """
        Xóa client khỏi danh sách khi kết nối WebSocket bị đóng.
        """
        WebSocketServer.clients.remove(self)

    @classmethod
    def send_message(cls, message: str):
        """
        Gửi một thông điệp tới tất cả các client đang kết nối.
        """
        print(f"Đang gửi thông điệp '{message}' tới {len(cls.clients)} client.")
        for client in cls.clients:
            client.write_message(message)

class RandomWordSelector:
    """
    Lớp chọn ngẫu nhiên các từ từ một danh sách.
    """
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        """
        Chọn ngẫu nhiên một từ từ danh sách.
        """
        return random.choice(self.word_list)

def main():
    """
    Hàm chính thiết lập và chạy WebSocket server.
    """
    # Cấu hình ứng dụng Tornado
    app = tornado.web.Application(
        [(r"/websocket/", WebSocketServer)],  # Định nghĩa route cho WebSocket
        websocket_ping_interval=10,
        websocket_ping_timeout=30,
    )
    app.listen(8888)

    # Tạo vòng lặp I/O
    io_loop = tornado.ioloop.IOLoop.current()

    # Khởi tạo RandomWordSelector với danh sách từ
    word_selector = RandomWordSelector(['apple', 'banana', 'orange', 'grape', 'melon'])

    # Gửi từ ngẫu nhiên tới client định kỳ mỗi 3 giây
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 3000
    )
    periodic_callback.start()

    # Bắt đầu vòng lặp sự kiện
    io_loop.start()

if __name__ == "__main__":
    main()
