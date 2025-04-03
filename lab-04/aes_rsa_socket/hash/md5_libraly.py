import hashlib

def calculate_md5(input_string):
    """
    Tính toán mã băm MD5 từ chuỗi đầu vào.
    """
    md5_hash = hashlib.md5()  # Khởi tạo đối tượng MD5
    md5_hash.update(input_string.encode('utf-8'))  # Mã hóa chuỗi sang UTF-8 và cập nhật vào MD5
    return md5_hash.hexdigest()  # Trả về kết quả mã băm dưới dạng chuỗi hexa

if __name__ == "__main__":
    input_string = input("Nhập chuỗi cần băm: ")  # Nhập chuỗi từ người dùng
    md5_hash = calculate_md5(input_string)  # Tính mã băm MD5
    print(f"Mã băm MD5 của chuỗi '{input_string}' là: {md5_hash}")  # Hiển thị kết quả
