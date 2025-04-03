import base64

def main():
    try:
        with open("data.txt", "r") as file:
            encoded_string = file.read()

        encoded_bytes = encoded_string.encode("utf-8")
        decoded_bytes = base64.b64decode(encoded_bytes)
        decoded_string = decoded_bytes.decode("utf-8")

        print("Thông tin đã giải mã: ", decoded_string)
    except Exception as e:
        print("Có lỗi xảy ra: ", e)

if __name__ == "__main__":
    main()
