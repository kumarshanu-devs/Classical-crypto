import oqs

def demo_kyber_encapsulation():
    with oqs.KeyEncapsulation('Kyber512') as kem:
        public_key = kem.generate_keypair()
        ciphertext, shared_secret_sender = kem.encap_secret(public_key)
        shared_secret_receiver = kem.decap_secret(ciphertext)

        print("Public Key:", public_key.hex()[:60] + "...")
        print("Ciphertext:", ciphertext.hex()[:60] + "...")
        print("Shared Secret (Sender):", shared_secret_sender.hex())
        print("Shared Secret (Receiver):", shared_secret_receiver.hex())

        assert shared_secret_sender == shared_secret_receiver

if __name__ == "__main__":
    demo_kyber_encapsulation()