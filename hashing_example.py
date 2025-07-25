import hashlib

def get_hash(text, algo='sha256'):
    h = hashlib.new(algo)
    h.update(text.encode('utf-8'))
    return h.hexdigest()

if __name__ == "__main__":
    text = "HelloHash"
    print(f"SHA256: {get_hash(text)}")
    print(f"MD5: {get_hash(text, 'md5')}")