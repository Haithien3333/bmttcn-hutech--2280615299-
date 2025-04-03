from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_server_key_pair(parameters):
    # Tạo khóa riêng tư và khóa công khai Diffie-Hellman
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    # Sinh tham số Diffie-Hellman
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    
    # Sinh khóa riêng tư và công khai
    private_key, public_key = generate_server_key_pair(parameters)
    
    # Ghi khóa công khai vào file
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

if __name__ == "__main__":
    main()
