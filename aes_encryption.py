from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_AES(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return cipher.iv + ct_bytes

def decrypt_AES(cipher_text, key):
    iv = cipher_text[:16]
    ct = cipher_text[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()

if __name__ == "__main__":
    key = get_random_bytes(16)
    text = "SecretAESMessage"
    ct = encrypt_AES(text, key)
    print(f"Decrypted: {decrypt_AES(ct, key)}")