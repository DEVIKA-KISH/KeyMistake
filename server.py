#!/usr/bin/env python3
import socket
import threading

FLAG = open("flag.txt", "r").read().strip()
KEY = b"superweakkey"

def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def handle_client(conn, addr):
    conn.sendall(b"Welcome to KeyMistake++\n")
    conn.sendall(b"We intercepted this encrypted message:\n")

    known_plain = b"This is a known message to help you recover the key."
    known_enc = xor_bytes(known_plain, KEY)
    conn.sendall(b"Known ciphertext (hex): " + known_enc.hex().encode() + b"\n")
conn.sendall(b"Known plaintext: This is a known message to help you recover the key.\n")

    conn.sendall(b"Hint: XOR the known plaintext with ciphertext to recover the key.\n")
    
    conn.sendall(b"\nEnter decrypted flag: ")
    user_input = conn.recv(1024).strip()

    if user_input.decode() == FLAG:
        conn.sendall(b" Correct! Well done. Here's your flag: " + FLAG.encode() + b"\n")
    else:
        conn.sendall(b" Incorrect. Try again.\n")

    conn.close()

def start_server():
    host = '0.0.0.0'
    port = 1337
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Listening on port {port}...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
