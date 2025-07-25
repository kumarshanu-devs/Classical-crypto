from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_keys():
    key = RSA.generate(2048)
    return key.export_key(), key.publickey().export_key()

def sign_message(message, private_key_bytes):
    private_key = RSA.import_key(private_key_bytes)
    h = SHA256.new(message.encode())
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

def verify_signature(message, signature, public_key_bytes):
    public_key = RSA.import_key(public_key_bytes)
    h = SHA256.new(message.encode())
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    private_key, public_key = generate_keys()
    msg = "This is a signed message."
    sig = sign_message(msg, private_key)
    valid = verify_signature(msg, sig, public_key)
    print(f"Signature valid? {valid}")