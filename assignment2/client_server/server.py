import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Secret key for AES (must be 16, 24, or 32 bytes)
SECRET_KEY = b'mysecretaeskey!!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created!")

port = 12345

s.bind(("", port))
print(f"Socket is binded to port {port}")

s.listen(5)
print("Socket is listening")

conn, addr = s.accept()
with conn:
    print(f"Connected by {addr}")
    while True:
        # Receive encrypted data
        encrypted_data = conn.recv(1024)
        if not encrypted_data:
            break
        
        # Decrypt the received data
        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, encrypted_data[:16])  # Extract IV
        decrypted_data = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
        
        # Process the decrypted data
        response = decrypted_data.decode().upper()[::-1]
        print(f"Received and processed: {response}")
        
        # Encrypt the response
        iv = get_random_bytes(16)  # Generate a new IV
        cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
        encrypted_response = iv + cipher.encrypt(pad(response.encode(), AES.block_size))
        
        # Send the encrypted response back
        conn.sendall(encrypted_response)
