def left_rotate(value, shift):
    """
    Xoay trái giá trị 32-bit.
    """
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5_hash(message):
    """
    Triển khai thuật toán MD5 để băm một chuỗi đầu vào.
    """
    # Các hằng số khởi tạo
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476
    # Tiền xử lý
    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += (original_length * 8).to_bytes(8, 'little')

    # Chia thành từng khối 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        # Lưu trạng thái ban đầu
        aa, bb, cc, dd = a, b, c, d

        # Vòng lặp chính của MD5
        for j in range(64):
            if j < 16:
                f = (b & c) | (~b & d)
                g = j
            elif j < 32:
                f = (d & b) | (~d & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * j) % 16

            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + f + words[g]) & 0xFFFFFFFF, (7, 12, 17, 22)[j % 4])) & 0xFFFFFFFF
            a = temp

        # Cộng dồn trạng thái
        a = (a + aa) & 0xFFFFFFFF
        b = (b + bb) & 0xFFFFFFFF
        c = (c + cc) & 0xFFFFFFFF
        d = (d + dd) & 0xFFFFFFFF

    # Kết quả cuối cùng
    return (a.to_bytes(4, 'little') +
            b.to_bytes(4, 'little') +
            c.to_bytes(4, 'little') +
            d.to_bytes(4, 'little')).hex()

if __name__ == "__main__":
    input_string = input("Nhập chuỗi cần băm: ")
    hash_result = md5_hash(input_string.encode('utf-8'))
    print(f"Mã băm MD5 của chuỗi '{input_string}' là: {hash_result}")
