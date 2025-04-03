from Crypto.Hash import SHA3_256

def sha3_hash(message):
    """
    Hàm tạo băm SHA-3 từ thông điệp đầu vào.
    """
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    """
    Hàm chính để nhận chuỗi đầu vào và tính toán giá trị băm.
    """
    # Nhập chuỗi văn bản từ người dùng
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')

    # Tính giá trị băm SHA-3
    hashed_text = sha3_hash(text)

    # Hiển thị kết quả
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("SHA-3 Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()
