from flask import Flask, request, jsonify

app = Flask(__name__)

def caesar_cipher(text, key, decrypt=False):
    result = ""
    shift = -key if decrypt else key
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

@app.route('/api/caesar/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    plain_text = data.get("plain_text", "")
    key = int(data.get("key", 0))
    encrypted_message = caesar_cipher(plain_text, key)
    return jsonify({"encrypted_message": encrypted_message})

@app.route('/api/caesar/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    cipher_text = data.get("cipher_text", "")
    key = int(data.get("key", 0))
    decrypted_message = caesar_cipher(cipher_text, key, decrypt=True)
    return jsonify({"decrypted_message": decrypted_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
