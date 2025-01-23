import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Secret key for AES (must match the server's key)
SECRET_KEY = b'mysecretaeskey!!'

HOST = "127.0.0.1"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    message = input("Enter your message: ").lower()
    
    iv = get_random_bytes(16)  # Generate a random IV
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    encrypted_message = iv + cipher.encrypt(pad(message.encode(), AES.block_size))
    
    s.sendall(encrypted_message)
    
    encrypted_response = s.recv(1024)
    
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, encrypted_response[:16])  # Extract IV
    decrypted_response = unpad(cipher.decrypt(encrypted_response[16:]), AES.block_size)
    
    print(f"Sent data (encrypted response): {encrypted_response}")
    print(f"Sent data (decrypted response): {decrypted_response.decode()}")
