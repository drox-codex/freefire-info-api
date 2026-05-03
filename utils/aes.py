from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt_response(encrypted_data, key=b"ST4Y_H4PPY_@LWAY"): 
    """
    Standard AES Decryption for Free Fire binary responses.
    Note: Key is usually 16-byte fixed or derived.
    """
    try:
        # This logic varies by specific FF API version
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = cipher.decrypt(encrypted_data)
        return unpad(decrypted, AES.block_size)
    except Exception:
        return encrypted_data