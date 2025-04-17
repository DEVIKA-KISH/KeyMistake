# KeyMistake
Cryptography-based XOR CTF challenge demonstrating key reuse vulnerability


# KeyMistake — Cryptography CTF Challenge

We've intercepted an encrypted message and its corresponding plaintext. Unfortunately, the attacker reused the same XOR key to encrypt another sensitive message — the **FLAG**.

Can you recover the key and decrypt the flag?

---
# HOW TO PLAY
- Connect to the challenge server using:
- nc <your_ip_or_ngrok_url> 1337
+ Clone this repo and run the challenge locally:
+ 
+ ```bash
+ git clone https://github.com/yourusername/KeyMistake-Room.git
+ cd KeyMistake-Room
+ python3 server.py
+ ```
+
+ Then in another terminal:
+
+ ```bash
+ nc 127.0.0.1 1337
+ ```






##  Objective

1. Use the known plaintext and the provided ciphertext to recover the XOR key
2. Use the recovered key to decrypt the `encrypted_flag.bin` file
3. Capture and submit the flag

---

##  Flag Format

```
flag{your_decrypted_flag_here}
```

## Files Provided

- server.py – Netcat-based CTF server
- xor_encryptor.py – File used to generate encrypted outputs
- flag.txt – Secret flag (used internally)
- encrypted_flag.bin – The XOR-encrypted flag
- known_plaintext.txt – Original known message
- known_encrypted.txt – Encrypted version of the known message
- README.txt – Player instructions (used in terminal)
- challenge_description.md – Academic write-up
- KeyMistake_CTF_Presentation.pptx – Presentation slides

---

##  What You Learn

- XOR encryption basics
- How key reuse makes XOR breakable
- Performing known-plaintext attacks
- Basic cryptanalysis

---

## Author

Devika Kishor  
M.S. Cybersecurity  
Florida Institute of Technology  
2025

```

---

