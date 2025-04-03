from PIL import Image
import sys

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    binary_message += '1111111111111110'  # Ký hiệu kết thúc thông điệp

    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))

            for color_channel in range(3):  # Xử lý 3 kênh màu RGB
                if data_index < len(binary_message):
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1

            img.putpixel((col, row), tuple(pixel))

            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = "encoded_image.png"
    img.save(encoded_image_path)
    print("Mã hóa hoàn tất! Ảnh đã lưu tại:", encoded_image_path)

def main():
    if len(sys.argv) != 3:
        print("Cách sử dụng: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()
