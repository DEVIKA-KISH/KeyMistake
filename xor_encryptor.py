def xor_encrypt(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

key = b"superweakkey"

with open("flag.txt", "rb") as f:
    flag = f.read()
with open("known_plaintext.txt", "rb") as f:
    known = f.read()
with open("partial_hint.txt", "rb") as f:
    partial = f.read()

with open("encrypted_flag.bin", "wb") as f:
    f.write(xor_encrypt(flag, key))
with open("known_encrypted.txt", "wb") as f:
    f.write(xor_encrypt(known, key))
with open("partial_hint.enc", "wb") as f:
    f.write(xor_encrypt(partial, key))
