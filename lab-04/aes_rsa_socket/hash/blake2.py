import hashlib

def blake2_hash(message):
    """
    Hàm tính giá trị băm BLAKE2b từ thông điệp đầu vào.
    """
    # Khởi tạo đối tượng băm BLAKE2b với kích thước đầu ra 64 byte
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)  # Cập nhật thông điệp vào đối tượng băm
    return blake2_hash.digest()  # Trả về giá trị băm (dạng bytes)

def main():
    """
    Hàm chính để lấy thông điệp từ người dùng và hiển thị giá trị băm.
    """
    # Nhập thông điệp từ người dùng
    text = input("Nhập chuỗi văn bản: ")
    message = text.encode('utf-8')  # Mã hóa chuỗi thành dạng bytes

    # Tính giá trị băm BLAKE2b
    hashed_message = blake2_hash(message)

    # Hiển thị kết quả
    print("Chuỗi văn bản đã nhập:", text)
    print("BLAKE2 Hash:", hashed_message.hex())  # Chuyển giá trị băm sang chuỗi hexa

if __name__ == "__main__":
    main()
