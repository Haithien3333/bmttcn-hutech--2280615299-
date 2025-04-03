from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def generate_client_key_pair(parameters):
    """
    Tạo cặp khóa Diffie-Hellman cho client.
    """
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    """
    Sinh ra shared secret từ khóa riêng của client và
    khóa công khai từ server.
    """
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():

    # Tải khóa công khai từ tệp PEM
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Lấy tham số từ khóa công khai của server
    parameters = server_public_key.parameters()

    # Tạo cặp khóa cho client
    private_key, public_key = generate_client_key_pair(parameters)

    # Sinh shared secret
    shared_secret = derive_shared_secret(private_key, server_public_key)

    # Hiển thị shared secret dưới dạng chuỗi hexa
    print("Shared Secret:", shared_secret.hex())

if __name__ == "__main__":
    main()
