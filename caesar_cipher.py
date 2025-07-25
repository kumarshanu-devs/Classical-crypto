def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    text = "HelloWorld"
    shift = 3
    encrypted = encrypt(text, shift)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypt(encrypted, shift)}")