🔐 Cryptography Basics in Python

This repository contains implementations of foundational and modern cryptographic algorithms using Python. It is designed to demonstrate both **core knowledge of classical cryptography** and awareness of **emerging post-quantum cryptographic standards**.

---

## 📁 Repository Structure

### 🧱 Classical Cryptographic Algorithms

| File | Description |
|------|-------------|
| `caesar_cipher.py` | Implements the classic Caesar Cipher with customizable shift. |
| `vigenere_cipher.py` | Vigenère Cipher encryption and decryption using a repeating key. |
| `rsa_example.py` | RSA key generation, encryption, and decryption using `pycryptodome`. |
| `aes_encryption.py` | AES encryption and decryption in CBC mode using `pycryptodome`. |
| `hashing_example.py` | Demonstrates SHA256 and MD5 hashing using Python’s `hashlib` module. |

Each file is accompanied by a corresponding `.txt` document briefly explaining its logic and use cases.

---

### 🧠 Post-Quantum Cryptography (PQC)

With quantum computing on the rise, traditional algorithms like RSA and ECC are becoming vulnerable. This repo introduces **Post-Quantum Cryptography**, backed by NIST's ongoing standardization.

| File | Description |
|------|-------------|
| `post_quantum_notes.txt` | A well-researched overview of PQC, NIST algorithms, and links to resources. |
| `pqc_kyber_demo.py` | A demo of Kyber512 key encapsulation using the `pyoqs` library (Open Quantum Safe). |
| `pqc_kyber_demo.txt` | Explanation of the Kyber demo, how to run it, and install requirements. |

#### To install `pyoqs`:
```bash
pip install pyoqs
````

---

## 🧰 Requirements

Some scripts depend on third-party libraries:

```bash
pip install pycryptodome pyoqs
```

---

## 📚 Why This Repo?

This repository serves multiple purposes:

* Showcase strong understanding of classical cryptographic techniques.
* Highlight awareness of future-proof security trends (PQC).
* Provide reusable and easy-to-understand examples for learners and professionals.
* Be a solid portfolio piece for jobs, internships, or academic references.

---

## 🔗 References

* [NIST Post-Quantum Cryptography](https://csrc.nist.gov/Projects/post-quantum-cryptography)
* [Open Quantum Safe](https://openquantumsafe.org/)
* [PyCryptodome Documentation](https://pycryptodome.readthedocs.io/)
* [pyoqs GitHub](https://github.com/open-quantum-safe/liboqs-python)

---
