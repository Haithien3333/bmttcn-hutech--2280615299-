import hashlib

def calculate_sha256_hash(data):
    """
    Hàm tính giá trị băm SHA-256 từ chuỗi đầu vào.
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))  # Chuyển chuỗi sang bytes và cập nhật vào SHA-256
    return sha256_hash.hexdigest()  # Trả về giá trị hash dưới dạng chuỗi hexa

if __name__ == "__main__":
    data_to_hash = input("Nhập dữ liệu để băm SHA-256: ")  # Nhập dữ liệu từ người dùng
    hash_value = calculate_sha256_hash(data_to_hash)  # Tính giá trị băm
    print(f"Giá trị hash SHA-256: {hash_value}")  # In kết quả ra màn hình
