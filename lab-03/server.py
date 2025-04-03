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
    try:
        data = request.get_json()
        plain_text = data.get("plain_text", "")
        key = data.get("key", 0)
        
        if not plain_text or not isinstance(key, int):
            return jsonify({"error": "Invalid input. Ensure 'plain_text' is a string and 'key' is an integer."}), 400

        encrypted_message = caesar_cipher(plain_text, key)
        return jsonify({"encrypted_message": encrypted_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/rsa/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.get_json()
        cipher_text = data.get("cipher_text", "")
        key = data.get("key", 0)
        
        if not cipher_text or not isinstance(key, int):
            return jsonify({"error": "Invalid input. Ensure 'cipher_text' is a string and 'key' is an integer."}), 400

        decrypted_message = caesar_cipher(cipher_text, key, decrypt=True)
        return jsonify({"decrypted_message": decrypted_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
