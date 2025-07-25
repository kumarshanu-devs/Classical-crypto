from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_message(message, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted = cipher.encrypt(message.encode())
    return binascii.hexlify(encrypted)

def decrypt_message(ciphertext, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted = cipher.decrypt(binascii.unhexlify(ciphertext))
    return decrypted.decode()

if __name__ == "__main__":
    private, public = generate_keys()
    message = "This is a secret message"
    encrypted = encrypt_message(message, public)
    decrypted = decrypt_message(encrypted, private)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")