import oqs

def falcon_sign_verify():
    with oqs.Signature("Falcon-512") as signer:
        public_key = signer.generate_keypair()
        message = b"Post-quantum signature example using Falcon-512."
        signature = signer.sign(message)
        valid = signer.verify(message, signature, public_key)
        print(f"Signature valid? {valid}")

if __name__ == "__main__":
    falcon_sign_verify()