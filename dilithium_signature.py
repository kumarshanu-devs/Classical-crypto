import oqs

def dilithium_sign_verify():
    with oqs.Signature("Dilithium2") as signer:
        public_key = signer.generate_keypair()
        message = b"Post-quantum signature example using Dilithium2."
        signature = signer.sign(message)
        valid = signer.verify(message, signature, public_key)
        print(f"Signature valid? {valid}")

if __name__ == "__main__":
    dilithium_sign_verify()