from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class AESCipher:
    def __init__(self, key: str, iv: str):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')

    def encrypt(self, raw_text: str) -> str:
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        padded_data = pad(raw_text.encode('utf-8'), AES.block_size)
        encrypted = cipher.encrypt(padded_data)
        return base64.b64encode(encrypted).decode('utf-8')

    def decrypt(self, encrypted_text: str) -> str:
        encrypted_bytes = base64.b64decode(encrypted_text)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
        return decrypted_data.decode('utf-8')