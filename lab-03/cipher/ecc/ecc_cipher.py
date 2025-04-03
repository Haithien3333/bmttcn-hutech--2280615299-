import ecdsa
import os


if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Sinh khóa riêng tư và công khai
        private_key = ecdsa.SigningKey.generate()
        public_key = private_key.get_verifying_key()
        # Lưu khóa riêng tư vào tệp
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as private_file:
            private_file.write(private_key.to_pem())
        # Lưu khóa công khai vào tệp
        with open('cipher/ecc/keys/publicKey.pem', 'wb') as public_file:
            public_file.write(public_key.to_pem())
        return private_key, public_key

    def load_keys(self):
        # Nạp khóa riêng tư từ tệp
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as private_file:
            private_key = ecdsa.SigningKey.from_pem(private_file.read())
        # Nạp khóa công khai từ tệp
        with open('cipher/ecc/keys/publicKey.pem', 'rb') as public_file:
            public_key = ecdsa.VerifyingKey.from_pem(public_file.read())
        return private_key, public_key

    def sign(self, message, private_key):
        # Ký thông điệp bằng khóa riêng tư
        return private_key.sign(message.encode('ascii'))

    def verify(self, message, signature, public_key):
        try:
            # Xác thực chữ ký bằng khóa công khai
            return public_key.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False
